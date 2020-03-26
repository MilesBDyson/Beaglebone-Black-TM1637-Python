import tm1637
import Adafruit_BBIO.GPIO as GPIO
import time

# CLK == Shared P9_12
# DIO == GPIO PIN P9_23
# GND == External Power
# 5v  == External Power

GPIO.setup("P9_12", GPIO.OUT)
GPIO.output("P9_12", GPIO.LOW)

disp = tm1637.TM1637("P9_12", "P9_23")

disp.set_brightness(0)
disp.set_doublepoint(False)
spin = 0

try:
    for i in range(0, 4):
        for j in range(0, 2):
            for s in ['S7', 'S3', 'S4', 'S5']:
                values = [' ', ' ', ' ', ' ']
                for k in range(0, i):
                    values[k] = 'o'
                values[i] = s
                disp.set_values(values)
                #time.sleep(0.1)
    disp.set_values(['o', 'o', 'o', 'o'])
except KeyboardInterrupt:
    pass

disp.cleanup()
