#!/usr/bin/env python3

import sys
import nxt.bluesock
from nxt.motor import *


def spin_around(b):
    m_left = Motor(b, PORT_B)
    m_left.turn(127, 360)
    m_right = Motor(b, PORT_C)
    m_right.turn(127, 360)


b = None
try:
    b = nxt.bluesock.BlueSock('00:16:53:08:09:1F').connect()
    spin_around(b)
except:
    print("Error while running test:")
    print(str(sys.exc_info()[1]))
    if b is not None:
        b.sock.close()
