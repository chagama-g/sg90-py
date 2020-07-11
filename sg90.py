import RPi.GPIO as GPIO


FREQ = 50


class SG90():
    def __init__(self, PIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)

        self.servo = GPIO.PWM(PIN, FREQ)

    def start(self):
        self.servo.start(0.0)

    def setDuty(self, duty):
        self.servo.ChangeDutyCycle(duty)

    def setDeg(self, deg):
        duty = (12-2.5) / 180 * deg + 2.5
        self.setDuty(duty)

    def cleanup(self):
        GPIO.cleanup()