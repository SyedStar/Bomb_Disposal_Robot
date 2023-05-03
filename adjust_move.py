# USAGE
# python detect_drowsiness.py --shape-predictor shape_predictor_68_face_landmarks.dat
# python detect_drowsiness.py --shape-predictor shape_predictor_68_face_landmarks.dat --alarm alarm.wav

# import the necessary packages

import time
import RPi.GPIO as GPIO
import pyttsx3
import urllib.request
import requests

right_1 = 19
right_2 = 26
left_1 = 6
left_2 = 13
gripper_1 = 10
gripper_2 = 9
move_1 = 11
move_2 = 5

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(right_1, GPIO.OUT)  # 
GPIO.setup(right_2, GPIO.OUT)
GPIO.setup(left_1, GPIO.OUT)
GPIO.setup(left_2, GPIO.OUT) 
GPIO.setup(gripper_1, GPIO.OUT)  # 
GPIO.setup(gripper_2, GPIO.OUT)
GPIO.setup(move_1, GPIO.OUT)
GPIO.setup(move_2, GPIO.OUT) 

def move_up():
            GPIO.output(move_1, False);
            GPIO.output(move_2, True);
            time.sleep(0.7);
            GPIO.output(move_1, False);
            GPIO.output(move_2, False);

# loop over frames from the video stream
while True:
  move_up()
  break

