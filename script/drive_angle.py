#!/usr/bin/env python3

import sys
from script.rolo_instance import rolo

try:
    r = rolo()
    r.turn_wheels(360)
    r.disconnect()
except IOError:
    print("Error while running test:")
    print(str(sys.exc_info()[1]))
    if b is not None:
        b.sock.close()
