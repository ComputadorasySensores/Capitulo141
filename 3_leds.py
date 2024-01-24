import wiringpi
import time
import sys
from wiringpi import GPIO

wiringpi.wiringPiSetup()
wiringpi.pinMode(25, GPIO.OUTPUT)
wiringpi.pinMode(23, GPIO.OUTPUT)
wiringpi.pinMode(22, GPIO.OUTPUT)

while True:
    try:
        wiringpi.digitalWrite(25, GPIO.HIGH)
        time.sleep(1)
        wiringpi.digitalWrite(25, GPIO.LOW)
        time.sleep(1)

        wiringpi.digitalWrite(23, GPIO.HIGH)
        time.sleep(1)
        wiringpi.digitalWrite(23, GPIO.LOW)
        time.sleep(1)

        wiringpi.digitalWrite(22, GPIO.HIGH)
        time.sleep(1)
        wiringpi.digitalWrite(22, GPIO.LOW)
        time.sleep(1)
    except KeyboardInterrupt:
        print("\n adios")
        wiringpi.digitalWrite(25, GPIO.LOW)
        wiringpi.digitalWrite(23, GPIO.LOW)
        wiringpi.digitalWrite(22, GPIO.LOW)
        sys.exit(0)