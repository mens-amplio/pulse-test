# This pulse demo uses modified code from the Metalab WS2801
# demo. Original license for that demo as follows:
#
# Simple Example for accessing WS2801 LED stripes
# Copyright (C) 2013  Philipp Tiefenbacher <wizards23@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# For more information about this project please visit:
# http://www.hackerspaceshop.com/ledstrips/raspberrypi-ws2801.html


import math
import time
from LedStrip_WS2801 import LedStrip_WS2801

# Modifiable parameters
color = [ 0, 100, 0 ]
delay = 0.5 #seconds between pulse onsets
step = 0.4 #raising this raises the speed. 0.1-0.7 is a good range.
dscale = .65 #raising this makes the pulse narrower. 0.3-1 is a good range.
leds = 6 #strip length

# RGB ordering of strip. 0=r, 1=g, 2=b
order = [ 1, 2, 0 ] 

def antialisedPoint(ledStrip, color, step, dscale, sleep = 0.01):
    rr = color[order[0]]
    gg = color[order[1]]
    bb = color[order[2]]
    screenOffset = int(1.0/(step*dscale))+1
    for j in range(-screenOffset, int(ledStrip.nLeds/step + screenOffset)):
        for i in range(0, ledStrip.nLeds):
            delta = 1-abs(i-j*step)*dscale
            if delta < 0: delta = 0
            ledStrip.setPixel(i, [int(delta*rr), int(delta*gg), int(delta*bb)])
        ledStrip.update()
        time.sleep(sleep)

ledStrip = LedStrip_WS2801("/dev/spidev0.0", leds)
while True:
    antialisedPoint(ledStrip, color, step, dscale)
    time.sleep(delay)

