#!/usr/bin/env python3

import sys
import time
from script.rolo_instance import rolo

try:
    r = rolo()

    r.drive(100)
    time.sleep(5)
    r.halt()
    r.disconnect()
except IOError:
    print("Error while running test:")
    print(str(sys.exc_info()[1]))
    r.disconnect()
