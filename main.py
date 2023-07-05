# main.py

import pyb
from pyb import Pin, ADC, LED, Timer
from time import sleep_ms

LED(1).off()
LED(2).off()
LED(3).off()
LED(4).off()

def led_blink(t):
   LED(1).toggle() 
   LED(2).toggle() 
   LED(3).toggle() 
   LED(4).toggle() 

timer = Timer (1, freq=100)
timer.freq(0.5)
timer.callback(led_blink)

count = 0
while count < 1000:
   count += 1
   sleep_ms(10)
   timer.freq(abs(accel.x()))



# end program with all LEDs on to indicate program ran from cold start
LED(1).on()
LED(2).on()
LED(3).on()
LED(4).on()


