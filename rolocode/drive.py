#!/usr/bin/env python3

import sys
import nxt.bluesock
from nxt.motor import *


def run(motors, time):
    for motor in motors:
        motor.run(power=100)

    sleep(time)

    for motor in motors:
        motor.idle()

b = None
try:
    b = nxt.bluesock.BlueSock('00:16:53:08:09:1F').connect()
    motors = [Motor(b, PORT_B), Motor(b, PORT_C)]
    run(motors, 10)
except:
    print("Error while running test:")
    print(str(sys.exc_info()[1]))
    if b is not None:
        b.sock.close()
