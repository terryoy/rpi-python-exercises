import RPi.GPIO as GPIO
import time

ledPin = 4

GPIO.setmode(GPIO.BCM) # set Broadcom's pin numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # set led pin to OUTPUT mode
GPIO.output(ledPin, GPIO.HIGH) # pull up the pin

time.sleep(3)

GPIO.output(ledPin, GPIO.LOW) # pull down the pin


