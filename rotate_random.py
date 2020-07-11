import RPi.GPIO as GPIO
import random

import time

def getDutyfromDeg(deg):
    return ((12-2.5)/180*deg+2.5)

INTERVAL = 0.6
PIN = 18
FREQ = 50

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN, GPIO.OUT)
servo = GPIO.PWM(PIN, FREQ)

#init
servo.start(0.0)

duty0   = getDutyfromDeg(0)
duty90  = getDutyfromDeg(90)
duty180 = getDutyfromDeg(180)

# for i in range(2):
while True:
    deg = random.randint(0,180)
    duty = getDutyfromDeg(deg)
    print("{}deg".format(str(deg).rjust(3, ' ')))
    servo.ChangeDutyCycle(duty)
    time.sleep(INTERVAL)


GPIO.cleanup()