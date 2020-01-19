

class Rolo:

    def_power = 100

    def __init__(self, brick):
        assert brick is not None
        self.brick = brick
        self.wheels = [brick.motor_b, brick.motor_c]
        self.steering = brick.motor_a

    def drive(self, power=def_power):
        for motor in self.wheels:
            motor.run(power=power)

    def turn_wheels(self, angle, power=def_power):
        for motor in self.wheels:
            motor.turn(power, tacho_units=angle)

    def halt(self):
        for motor in self.wheels:
            motor.idle

    def disconnect(self):
        if self.is_connected():
            self.brick.sock.close()
            self.brick.sock = None

    def is_connected(self):
        self.brick.sock is not None

