
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 11
GPIO_ECHO = 18

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(GPIO_TRIG, GPIO.LOW)
        time.sleep(0.1)

        GPIO.output(GPIO_TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIG, GPIO.LOW)

        starttime = time.time()

        while GPIO.input(GPIO_ECHO) == 0:
            starttime = time.time()

        end = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            end = time.time()

        pulse_duration = end - starttime

        distance = round(pulse_duration * 17150, 2)

        print("Distance:", distance, "cm")

        time.sleep(1)

except KeyboardInterrupt:
    print("---Program ended---")

finally:
    GPIO.cleanup()
