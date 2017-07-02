#!/usr/bin/env python3

import struct
import time
import math
import glob
from ft5406 import Touchscreen, TS_PRESS, TS_RELEASE, TS_MOVE
from math import floor
from subprocess import call
import rpi_backlight as bl

def read_and_emulate_mouse(event, touch):
    global startX
    global startY
    global startTime
    global shouldRun

    if event == TS_PRESS:
        # print("Got Press", touch)
        (startX, startY) = touch.position
        startTime = time.time()
    # if event == TS_RELEASE:
    #     print("Got release", touch)
    # if event == TS_MOVE:
    #     print("Got move", touch.position)

    (x, y) = touch.position
    (last_x, last_y) = touch.last_position

    movement = math.sqrt(pow(x - startX, 2) + pow(y - startY, 2))
    # top left: brightness
    if startX < 10 and startY > 469 and x <= 200:
        call(["amixer", "cset", "numid=1", "--", str(floor(x/2)) + '%'])
    # bottom left: volume
    if startX < 10 and startY < 10 and x <= 244:
        bl.set_brightness(x + 11)
    # top right: quit parsec
    if startX > 788 and startY < 10:
        if movement < 20 and event == TS_RELEASE and (time.time() - startTime) >= 3:
            call(["killall", "parsec"])
            call(["killall", "screen"])
            call(["./touchscreen"])
            shouldRun = False
            exit()
    if startX > 788 and startY > 469:
        if movement < 20 and event == TS_RELEASE and (time.time() - startTime) >= 3:
            call(["killall", "screen"])
            call(["screen",  "-dm", "-S", "jcdriver", "./go/bin/jcdriver"])

if __name__ == "__main__":
    global shouldRun
    shouldRun = True
    ts = Touchscreen()

    for touch in ts.touches:
        touch.on_press = read_and_emulate_mouse
        touch.on_release = read_and_emulate_mouse
        touch.on_move = read_and_emulate_mouse

    ts.run()

    while shouldRun:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            ts.stop()
            exit()

    ts.stop()
    exit()