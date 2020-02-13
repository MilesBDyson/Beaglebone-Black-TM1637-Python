#!/usr/bin/python
import tm1637
from time import *
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_26", GPIO.OUT)
GPIO.setup("P8_18", GPIO.OUT)
GPIO.output("P8_26", GPIO.LOW)
GPIO.output("P8_18", GPIO.LOW)
disp=tm1637.TM1637("P8_7", "P8_9")
disp.clear()
x=True
L1='0'
L2='0'
L3='0'
L4='0'
Update=False
while True:
   hour=strftime('%I')
   minute=strftime('%M')
   ampm=strftime("%p")
   if hour[0]=='0':
      T1=' '
   else:
      T1=hour[0]
   T2=hour[1]
   T3=minute[0]
   T4=minute[1]
   if T1 != L1:
      L1=T1
      Update=True
   if T2 != L2:
      L2=T2
      Update=True
   if T3 != L3:
      L3=T3
      Update=True
   if T4 != L4:
      L4=T4
      Update=True
   if ampm == 'PM':
      GPIO.output("P8_18", GPIO.LOW)
      GPIO.output("P8_26", GPIO.HIGH)
   else:
      GPIO.output("P8_26", GPIO.LOW)
      GPIO.output("P8_18", GPIO.HIGH)
   if Update==True:
      Update=False
      disp.set_values([T1, T2, T3, T4])
   disp.set_doublepoint(x)
   if x==True:
      x=False
   else:
      x=True
