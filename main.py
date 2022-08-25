import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setwarnings(False)

response = None
while not (response == "on" or response == "off"):
    response = input("Do you want to turn on relay?").lower()

try:
    while True:
        if response == "on":
            GPIO.output(21, GPIO.LOW)
            time.sleep(2)
            print("It's ON")
        else:
            GPIO.output(21, GPIO.HIGH)
            time.sleep(2)
            print("It's OFF")

finally:
    GPIO.cleanup()
