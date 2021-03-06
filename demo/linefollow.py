#!/usr/bin/env python3
'''
EV3 follows a black line

Colour sensor must be attached, as well as large motors on ports B and C

Taken from Nigel Wards example
https://sites.google.com/site/ev3python/learn_ev3_python/basics/beyond-basics-ex-1-6
'''

from ev3dev.ev3 import *

btn = Button() # will use any button to stop script

# Connect EV3 color sensor and check connected.
cl = ColorSensor() 
assert cl.connected, "Connect a color sensor to any sensor port"

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode='COL-REFLECT'

# Attach large motors to ports B and C
mB = LargeMotor('outB')
mC = LargeMotor('outC')

while not btn.any():    # exit loop when any button pressed
  if cl.value()<30:   # weak reflection so over black line
    # medium turn right
    mB.run_forever(speed_sp=200)
    mC.stop(stop_action='brake')
  else:   # strong reflection (>=30) so over white surface
    # medium turn left
    mB.stop(stop_action='brake')
    mC.run_forever(speed_sp=200)
      
mB.stop(stop_action='brake')
mC.stop(stop_action='brake')
