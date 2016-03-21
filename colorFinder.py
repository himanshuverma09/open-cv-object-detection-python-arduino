import cv2, math
import numpy as np
import serial
import time



class hsv_find:
    def __init__(self):
        cv2.namedWindow("TrackBar") 
        self.capture = cv2.VideoCapture(1)
        self.scale_down = 4
        
    def run(self):
        
        def nothing(x):
            pass

        while True:
            f, orig_img = self.capture.read()    
            cv2.createTrackbar('H_MIN','TrackBar',0,255,nothing)
            cv2.createTrackbar('H_MAX','TrackBar',255,255,nothing)
            cv2.createTrackbar('S_MIN','TrackBar',0,255,nothing)
            cv2.createTrackbar('S_MAX','TrackBar',255,255,nothing)
            cv2.createTrackbar('V_MIN','TrackBar',0,255,nothing)
            cv2.createTrackbar('V_MAX','TrackBar',255,255,nothing)
              #switch = '0 : OFF \n1 : ON'
              #cv2.createTrackbar(switch, 'TrackBar',0,1,nothing)
            H_MIN = cv2.getTrackbarPos('H_MIN','TrackBar')
            H_MAX = cv2.getTrackbarPos('H_MAX','TrackBar')
            S_MIN = cv2.getTrackbarPos('S_MIN','TrackBar')
            S_MAX = cv2.getTrackbarPos('S_MAX','TrackBar')
            V_MIN = cv2.getTrackbarPos('V_MIN','TrackBar')
            V_MAX = cv2.getTrackbarPos('V_MAX','TrackBar')
              #Motor_Switch = cv2.getTrackbarPos(switch,'TrackBar')
            lower = np.array([H_MIN, S_MIN, V_MIN],np.uint8)
            upper = np.array([H_MAX, S_MAX, V_MAX],np.uint8)
            img = cv2.GaussianBlur(orig_img, (5,5), 0)
            img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
            img = cv2.resize(img, (len(orig_img[0]) / self.scale_down, len(orig_img) / self.scale_down))
            red_binary = cv2.inRange(img, lower, upper)
            dilation = np.ones((15, 15), "uint8")
            red_binary = cv2.dilate(red_binary, dilation)

            cv2.imshow("TrackBar", red_binary)
            cv2.waitKey(60)
   

      
if __name__ == "__main__":
    hsv = hsv_find()
    hsv.run()

            
