import tm1637
import Adafruit_BBIO.GPIO as GPIO

# Use the Enter key to display the next set of characters
# CLK == Shared P9_12
# DIO == GPIO PIN P9_23
# GND == External Power
# 5v  == External Power

disp = tm1637.TM1637("P9_12", "P9_23")

disp.clear()

disp.set_values(['A', 'B', 'b', 'C'])
r = raw_input()

disp.set_values(['c', 'D', 'd', 'E'])
r = raw_input()

disp.set_values(['F', 'G', 'H', 'h'])
r = raw_input()

disp.set_values(['I', 'J', 'K', 'L'])
r = raw_input()

disp.set_values(['l', 'n', 'O', 'o'])
r = raw_input()

disp.set_values(['P', 'r', 'S', 'U'])
r = raw_input()

disp.set_values(['Y', 'Z', ' ', ' '])
r = raw_input()

disp.set_values(['T1', 'T2', 'W1', 'W2'])
r = raw_input()

disp.set_value('M1', 0)
r = raw_input()

disp.set_value('M2', 1)
r = raw_input()

disp.clear()

x = True
for i in range(8):
    disp.set_doublepoint(x)
    disp.set_brightness(i)
    r = raw_input()
    x = not x

disp.clear()

disp.cleanup()
