import nxt.bluesock
from rolocode.rolo import Rolo

address = '00:16:53:08:09:1F'


def rolo():
    try:
        return Rolo(nxt.bluesock.BlueSock(address).connect())
    except IOError:
        print("Error while running test:")
        print(str(sys.exc_info()[1]))
        if b is not None:
            b.sock.close()
