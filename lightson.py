#!/usr/bin/env python

from gpiozero import LED
from time import sleep

star = LED(14)

lights = [LED(15), LED(18), LED(23), LED(24), LED(25), LED(8), LED(7), LED(12), LED(16), LED(20)]

star.on()

for i in range(10):
    sleep(0.1)
    lights[i].on()
