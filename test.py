import tm1637
from time import *

disp = tm1637.TM1637("P8_7", "P8_9")
disp.clear()
x = True
while True:
   hour = strftime('%I')
   T1=hour[0]
   T2=hour[1]
   minute = strftime('%M')
   T3=minute[0]
   T4=minute[1]
   disp.set_values([T1, T2, T3, T4])
   disp.set_doublepoint(x)
   if x == True:
      x = False
   else:
      x = True
