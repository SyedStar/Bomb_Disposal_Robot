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


GPIO_TRIGGER = 22
GPIO_ECHO = 27
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
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.say("A-I based Drowziness detection system")
engine.runAndWait()
                
def mot_stop():
            GPIO.output(right_1, False);
            GPIO.output(right_2, False);
            GPIO.output(left_1, False);
            GPIO.output(left_2, False);

def mot_start():
            GPIO.output(right_1, True);
            GPIO.output(right_2, False);
            GPIO.output(left_1, False);
            GPIO.output(left_2, True);

def mot_left():
            GPIO.output(right_1, False);
            GPIO.output(right_2, True);
            GPIO.output(left_1, False);
            GPIO.output(left_2, True);

def mot_right():
            GPIO.output(right_1, True);
            GPIO.output(right_2, False);
            GPIO.output(left_1, True);
            GPIO.output(left_2, False);

def mot_back():
            GPIO.output(right_1, False);
            GPIO.output(right_2, True);
            GPIO.output(left_1, True);
            GPIO.output(left_2, False);
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

# loop over frames from the video stream
while True:
    z=20
    y=distance()
    print("Distance = ")
    print(y)
    if y<10:
        mot_stop()
        print("Alert! Alert!  Obstacle detedted in front")
        engine = pyttsx3.init()
        engine.say("ALERT! Alert! Obstacle detedted in front")
        engine.runAndWait()
        time.sleep(4)
        z=10
    url = "https://airobosoft.com/2022/dispose/api/motor.php"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,} 
    request=urllib.request.Request(url,None,headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read() # The data u need
    data = data.decode()
    d=int(data)
    print(data)
    print('_____________________________________________')
    if d == 1:
        mot_start()
        print(d)
    elif d == 2:
        mot_back()
        print(d)
    elif d == 3:
        mot_right()
        print(d)
    elif d == 4:
        mot_left()
    elif d == 0:
        mot_stop()
