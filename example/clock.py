#!/usr/bin/python
import tm1637
from time import *
import Adafruit_BBIO.GPIO as GPIO

# CLK == Shared P9_12
# DIO == GPIO PIN P9_23
# GND == External Power
# 5v  == External Power

# Setup Pins for LED's used for Time (AM/PM)
GPIO.setup("P8_26", GPIO.OUT)
GPIO.setup("P8_18", GPIO.OUT)
GPIO.output("P8_26", GPIO.LOW)
GPIO.output("P8_18", GPIO.LOW)
# Display 1 (Time)
ShowTime=tm1637.TM1637("P9_12", "P9_23")
ShowTime.clear()
ShowTime.set_brightness(0)
# Declare Variables
x=True
LastTime1='0'
LastTime2='0'
LastTime3='0'
LastTime4='0'
UpdateTime=False
while True:
   # Get Current Time
   hour=strftime('%I')
   minute=strftime('%M')
   ampm=strftime("%p")
   if hour[0]=='0':
      Time1=' '
   else:
      Time1=hour[0]
   Time2=hour[1]
   Time3=minute[0]
   Time4=minute[1]
   # Check if Time Needs Updated 
   if Time1 != LastTime1:
      LastTime1=Time1
      UpdateTime=True
   if Time2 != LastTime2:
      LastTime2=Time2
      UpdateTime=True
   if Time3 != LastTime3:
      LastTime3=Time3
      UpdateTime=True
   if Time4 != LastTime4:
      LastTime4=Time4
      UpdateTime=True
   if ampm == 'PM':
      GPIO.output("P8_18", GPIO.LOW)
      GPIO.output("P8_26", GPIO.HIGH)
   else:
      GPIO.output("P8_26", GPIO.LOW)
      GPIO.output("P8_18", GPIO.HIGH)
   # Update Time as Needed
   if UpdateTime == True:
      UpdateTime=False
      ShowTime.set_values([Time1, Time2, Time3, Time4])
   # Flash Colon for Time
   ShowTime.set_doublepoint(x)
   if x==True:
      x=False
   else:
      x=True
