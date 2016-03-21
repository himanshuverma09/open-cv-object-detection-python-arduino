Code For laser guided machine using opencv, python and arduino.

What different files do:

1) >> python-opencv-object-detection.py
The python code captures video using a webcam or any other source (you have to manually provide video source in source code).
Python code sends singal to arduino using usb.

2) >> arduino.c
You have to flash the arduino.c in arduino. It will recieve the signal and based on those signals will run the motor.

3) >> colorFinder.py
This script helps you to find the hsv value for the desired color. Use the trackbar to adjust hsv value. When you find all the background black and your object white, thats the desired hsv value, copy it and put it in python-opencv-object-detection.py (by default it detects red object like laser light).



Check the running model here:
https://www.youtube.com/watch?v=aEcD4zZqIlc
