# pyboard1
check LED, accelerometer and peripherals
Pyboard Project: Rate of flashing of red, green, yellow LEDs is proportional to the acceleration in 3-space.
1. Implement simple LED flashing and run this program on power up automatically.
2. Sample the accelerometer every 100 ms to check the dynamic range while waving unit around with arms.  Can also put inside a ball to track acceleration of ball.
3. Set flashing rate between 1/second to 20/second representing dynamic range in 2.
4. Check code into GitHub and write up.

Connect MAC to Pyboard:
ls /dev | grep usb # shows devices mounted; look for pyboard in devices mounted and use to connect
screen /dev/tty.usbmodem3776366C33362 155200 
MicroPython v1.8.7-478-gbfb48c1 on 2017-03-24; PYBv1.1 with STM32F405RG

chatGPT code: “python code to blink an LED with rate proportional to an accelerometer reading and updated every 10 ms”
