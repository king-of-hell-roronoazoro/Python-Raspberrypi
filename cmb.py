import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIG = 11
GPIO_ECHO = 18
IR_PIN = 17
PIR_PIN = 27
SLOT_PIN = 22

GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(SLOT_PIN, GPIO.IN)

def get_distance():
    GPIO.output(GPIO_TRIG, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(GPIO_TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIG, GPIO.LOW)

    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        bounce_back_time = time.time()

    pulse_duration = bounce_back_time - start_time
    return round(pulse_duration * 17150, 2)

try:
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")

        if GPIO.input(IR_PIN) == 0:
            print("IR: Obstacle detected")
        else:
            print("IR: Clear")

        if GPIO.input(PIR_PIN) == 1:
            print("PIR: Motion detected")
        else:
            print("PIR: No motion")

        if GPIO.input(SLOT_PIN) == 1:
            print("Slot: Blocked")
        else:
            print("Slot: Open")

        print("-----")
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()