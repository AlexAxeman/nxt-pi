#!/usr/bin/env python3

import sys
import nxt.bluesock
import time
from rolocode.rolo import Rolo

try:
    b = nxt.bluesock.BlueSock('00:16:53:08:09:1F').connect()
    r = Rolo(b)

    time.sleep(5)
    r.drive(100)
    r.halt()
except:
    print("Error while running test:")
    print(str(sys.exc_info()[1]))
    if b is not None:
        b.sock.close()
