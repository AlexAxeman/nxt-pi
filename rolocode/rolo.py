

class Rolo:
    def __init__(self, brick):
        assert brick is not None
        self.brick = brick
        self.wheels = [brick.motor_b, brick.motor_c]
        self.steering = brick.brick_a

    def drive(self, power):
        for motor in self.wheels:
            motor.run(power=power)

    def halt(self):
        for motor in self.wheels:
            motor.idle


