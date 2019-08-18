#!/usr/bin/env python2

from gpiozero import LED
from time import sleep

# Use correct GPIO pin number
led = LED(17) 

# Blink LED every second until program exits
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
