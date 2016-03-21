#Author: Himanshu Verma

import cv2, math
import numpy as np
import serial
import time

arduino = serial.Serial('/dev/ttyACM2', 9600)
time.sleep(2) # waiting the initialization...
print("initialising")

class ColourTracker:
  def __init__(self):
    cv2.namedWindow("ColourTrackerWindow")
    
    
    self.capture = cv2.VideoCapture(1)
    self.scale_down = 4

  def run(self):

    def nothing(x):
      pass

    while True:
      time.sleep(0.05) # waiting the initialization...
      f, orig_img = self.capture.read()
      #orig_img = cv2.flip(orig_img, 1)
      #cv2.createTrackbar('H_MIN','TrackBar',0,255,nothing)
      #cv2.createTrackbar('H_MAX','TrackBar',255,255,nothing)
      #cv2.createTrackbar('S_MIN','TrackBar',0,255,nothing)
      #cv2.createTrackbar('S_MAX','TrackBar',255,255,nothing)
      #cv2.createTrackbar('V_MIN','TrackBar',0,255,nothing)
      #cv2.createTrackbar('V_MAX','TrackBar',255,255,nothing)
      #switch = '0 : OFF \n1 : ON'
      #cv2.createTrackbar(switch, 'TrackBar',0,1,nothing)
      #H_MIN = cv2.getTrackbarPos('H_MIN','TrackBar')
      #H_MAX = cv2.getTrackbarPos('H_MAX','TrackBar')
      #S_MIN = cv2.getTrackbarPos('S_MIN','TrackBar')
      #S_MAX = cv2.getTrackbarPos('S_MAX','TrackBar')
      #V_MIN = cv2.getTrackbarPos('V_MIN','TrackBar')
      #V_MAX = cv2.getTrackbarPos('V_MAX','TrackBar')
      #Motor_Switch = cv2.getTrackbarPos(switch,'TrackBar')
      lower = np.array([170, 0, 170],np.uint8)
      upper = np.array([255, 255, 255],np.uint8)
      img = cv2.GaussianBlur(orig_img, (5,5), 0)
      img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
      img = cv2.resize(img, (len(orig_img[0]) / self.scale_down, len(orig_img) / self.scale_down))
      red_binary = cv2.inRange(img, lower, upper)
      dilation = np.ones((15, 15), "uint8")
      red_binary = cv2.dilate(red_binary, dilation)
      

      contours, hierarchy = cv2.findContours(red_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      max_area = 0
      
      largest_contour = None
      for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > max_area:
          max_area = area
          largest_contour = contour
      if not largest_contour == None:
        moment = cv2.moments(largest_contour)
        if moment["m00"] > 1000 / self.scale_down:
          
          rect = cv2.minAreaRect(largest_contour)
          rect = ((rect[0][0] * self.scale_down, rect[0][1] * self.scale_down), (rect[1][0] * self.scale_down, rect[1][1] * self.scale_down), rect[2])
          box = cv2.cv.BoxPoints(rect)
          box = np.int0(box)
          
          centroid_x = int(moment['m10']/moment['m00'])
          centroid_y = int(moment['m01']/moment['m00'])
          #if Motor_Switch==1:
            #print 'ON'
          if centroid_x > 100:
            print 'Right'
            arduino.write('R')
          elif centroid_x < 60:
            print 'Left'
            arduino.write('L')
          else:
            print 'Stop'
            arduino.write('X')
            
                     
          if centroid_y < 45:
            arduino.write('U')
            print 'up'
          elif centroid_y > 75:
            arduino.write('D')
            print 'Down'
          else:
            arduino.write('Y')
            print 'Stop'


          
          arduino.write('Y')
          arduino.write('X')
          
          
            
          cv2.drawContours(orig_img,[box], 0, (0, 0, 255), 2)

      else:
        arduino.write('Y')
        arduino.write('X')
        


      cv2.imshow("ColourTrackerWindow", orig_img)


      if cv2.waitKey(20) == 27:
        cv2.destroyWindow("ColourTrackerWindow")
        
        self.capture.release()
        break


      
if __name__ == "__main__":
  colour_tracker = ColourTracker()
  colour_tracker.run()
