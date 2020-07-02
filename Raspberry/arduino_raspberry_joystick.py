import RPi.GPIO as GPIO
import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

GPIO.setmode(GPIO.BCM)
RED = 26; BLUE = 13; GREEN = 19

GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, 0)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(GREEN, 0)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(BLUE, 0)

ser = serial.Serial(port, baudrate=brate, timeout = None)
print(ser.name)

if __name__ == '__main__':
    while True:
        try:
            if ser.in_waiting != 0:
                content = ser.readline()
                content = content.decode('utf-8').replace('\r\n','')
                vals = content.split(':')
                if len(vals) < 3:
                    continue
                print(vals)
                if vals[0] == '0':
                    GPIO.output(RED, GPIO.LOW)
                elif vals[0] == '1023':
                    GPIO.output(RED, GPIO.HIGH)
                if vals[1] == '0':
                    GPIO.output(GREEN, GPIO.LOW)
                elif vals[1] == '1023':
                    GPIO.output(GREEN, GPIO.HIGH)
                if vals[2] == '1':
                    GPIO.output(BLUE, GPIO.LOW)
                elif vals[2] == '0':
                    GPIO.output(BLUE, GPIO.HIGH)
        except KeyboardInterrupt:
            GPIO.cleanup()