#!/usr/bin/env python3

import struct
import time
import math
import glob
import uinput
import pyudev
import os
from ft5406 import Touchscreen, TS_PRESS, TS_RELEASE, TS_MOVE
from math import floor

def read_and_emulate_mouse(event, touch):
    global startX
    global startY
    global startTime
    global mouse

    if event == TS_PRESS:
        # print("Got Press", touch)
        (startX, startY) = touch.position
        startTime = time.time()
    # if event == TS_RELEASE:
    #     print("Got release", touch)
    # if event == TS_MOVE:
    #     print("Got move", touch)

    (x, y) = touch.position
    (last_x, last_y) = touch.last_position

    movement = math.sqrt(pow(x - startX, 2) + pow(y - startY, 2))
    if movement < 20:
        if event == TS_RELEASE:
            duration = time.time() - startTime
            if duration > 1:
                print("Right click")
                mouse.emit(uinput.BTN_RIGHT, 1)
                mouse.emit(uinput.BTN_RIGHT, 0)
                (startX, startY) = touch.position
            else:
                print("Left click")
                mouse.emit(uinput.BTN_LEFT, 1)
                mouse.emit(uinput.BTN_LEFT, 0)
                (startX, startY) = touch.position
    else:
        mouse.emit(uinput.REL_X, x - last_x, syn=False)
        mouse.emit(uinput.REL_Y, y - last_y)

if __name__ == "__main__":
    global mouse

    os.system("modprobe uinput")
    #os.system("chmod 666 /dev/hidraw*")
    os.system("chmod 666 /dev/uinput*")

    mouse = uinput.Device([
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        uinput.REL_X,
        uinput.REL_Y,
    ])

    ts = Touchscreen()

    for touch in ts.touches:
        touch.on_press = read_and_emulate_mouse
        touch.on_release = read_and_emulate_mouse
        touch.on_move = read_and_emulate_mouse

    ts.run()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            ts.stop()
            exit()