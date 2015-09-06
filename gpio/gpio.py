# This program turns on the LED on pin 4 for 3 seconds and then turn off

import RPi.GPIO as GPIO
import time

ledPin = 4 # define the LED pin

GPIO.setmode(GPIO.BCM) # set Broadcom's pin numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # set led pin to OUTPUT mode
GPIO.output(ledPin, GPIO.HIGH) # pull up the pin

time.sleep(3) # wait for 3 seconds

GPIO.output(ledPin, GPIO.LOW) # pull down the pin


