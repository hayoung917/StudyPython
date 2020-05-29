import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)    #GREEN
GPIO.setup(20, GPIO.OUT)    #RED

try:
    while True:
        GPIO.output(20,True)    #RED ON
        GPIO.output(21,False)   #GREEN OFF
        time.sleep(1)

        GPIO.output(20,False)    #RED OFF
        GPIO.output(21,True)     #GREEN ON
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
