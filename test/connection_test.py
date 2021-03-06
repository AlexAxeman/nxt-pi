#!/usr/bin/env python3

import nxt.bluesock # Make sure you remember this!

b = None
try:
    print('Find brick...', flush=True)
    b = nxt.bluesock.BlueSock('00:16:53:08:09:1F').connect()
    name, host, signal_strength, user_flash = b.get_device_info()
    print('NXT brick name: %s' % name)
    print('Host address: %s' % host)
    print('Bluetooth signal strength: %s' % signal_strength)
    print('Free user flash: %s' % user_flash)
    prot_version, fw_version = b.get_firmware_version()
    print('Protocol version %s.%s' % prot_version)
    print('Firmware version %s.%s' % fw_version)
    millivolts = b.get_battery_level()
    print('Battery level %s mV' % millivolts)
    print('Play test sound...', end='', flush=True)
    b.play_tone_and_wait(300, 50)
    b.play_tone_and_wait(400, 50)
    b.play_tone_and_wait(500, 50)
    b.play_tone_and_wait(600, 50)
    print('done')
    b.sock.close()
except:
    print("Error while running test:")
    traceback.print_tb(sys.exc_info()[2])
    print(str(sys.exc_info()[1]))
    if b is not None:
        b.sock.close()

