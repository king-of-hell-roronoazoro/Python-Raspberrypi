import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

irsensor = 3
GPIO.setup(irsensor, GPIO.IN)
try:
    while True:
        sensorval = GPIO.input(irsensor)
        if sensorval==0:
            print("Not motion detected!")
        else:
            print("Obj detected!")
        time.sleep(2)
except KeyboardInterrupt:
    print("---program ended---")
finally:
    GPIO.cleanup()