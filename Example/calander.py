#!/usr/bin/python
import tm1637
from time import *
import Adafruit_BBIO.GPIO as GPIO

# CLK == Shared P9_12
# DIO == GPIO PIN P9_23
# GND == External Power
# 5v  == External Power

# Setup the pins for two LED's (AM/PM)
GPIO.setup("P8_8", GPIO.OUT)
GPIO.output("P8_8", GPIO.LOW)
GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.LOW)
GPIO.setup("P8_12", GPIO.OUT)
GPIO.output("P8_12", GPIO.LOW)
GPIO.setup("P8_14", GPIO.OUT)
GPIO.output("P8_14", GPIO.LOW)
# Display 1 (Time)
ShowTime=tm1637.TM1637("P9_12", "P9_23")
# Display 2 (Date)
ShowDate=tm1637.TM1637("P9_12", "P9_25")
# Display 3 (Year)
ShowYear=tm1637.TM1637("P9_12", "P9_27")
# Clear all Displays
ShowTime.clear()
ShowDate.clear()
ShowYear.clear()
# Set Brightness of all Displays
ShowTime.set_brightness(2)
ShowDate.set_brightness(2)
ShowYear.set_brightness(2)
# Declare Variables
x=True
LastTime1='0'
LastTime2='0'
LastTime3='0'
LastTime4='0'
LastDate1='0'
LastDate2='0'
LastDate3='0'
LastDate4='0'
LastYear1='0'
LastYear2='0'
LastYear3='0'
LastYear4='0'
UpdateTime=False
UpdateDate=False
UpdateYear=False

while True:
   # Get Current Time
   hour=strftime('%I')
   minute=strftime('%M')
   ampm=strftime("%p")
   #if hour[0]=='0':
   #   Time1=' '
   #else:
   #   Time1=hour[0]
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
      GPIO.output("P8_14", GPIO.LOW)
      GPIO.output("P8_12", GPIO.HIGH)
   else:
      GPIO.output("P8_12", GPIO.LOW)
      GPIO.output("P8_14", GPIO.HIGH)
   # Get Current Date
   day=strftime('%d')
   month=strftime('%m')
   #if month[0]=='0':
   #   Date1=' '
   #else:
   #   Date1=month[0]
   Date1=month[0]
   Date2=month[1]+"."
   #if day[0]=='0':
   #   Date3=' '
   #else:
   #   Date3=day[0]
   Date3=day[0]
   Date4=day[1]
   # Check if Date Needs Updated
   if Date1 != LastDate1:
      LastDate1=Date1
      UpdateDate=True
   if Date2 != LastDate2:
      LastDate2=Date2
      UpdateDate=True
   if Date3 != LastDate3:
      LastDate3=Date3
      UpdateDate=True
   if Date4 != LastDate4:
      LastDate4=Date4
      UpdateDate=True
   # Get Current Year
   year=strftime('%Y')
   Year1=year[0]
   Year2=year[1]
   Year3=year[2]
   Year4=year[3]+"."
   # Check if Year Needs Updated
   if Year1 != LastYear1:
      LastYear1=Year1
      UpdateYear=True
   if Year2 != LastYear2:
      LastYear2=Year2
      UpdateYear=True
   if Year3 != LastYear3:
      LastYear3=Year3
      UpdateYear=True
   if Year4 != LastYear4:
      LastYear4=Year4
      UpdateYear=True
   # Update All Displays as Needed
   if UpdateTime==True:
      UpdateTime=False
      ShowTime.set_values([Time1, Time2, Time3, Time4])
   if UpdateDate==True:
      UpdateDate=False
      ShowDate.set_values([Date1, Date2, Date3, Date4])
   if UpdateYear==True:
      UpdateYear=False
      ShowYear.set_values([Year1, Year2, Year3, Year4])
   # Flash Colon On Time Display
   ShowTime.set_doublepoint(x)
   if x==True:
      x=False
   else:
      x=True

ShowTime.clear()
ShowTime.cleanup()
ShowDate.clear()
ShowDate.cleanup()
ShowYear.clear()
ShowYear.cleanup()
