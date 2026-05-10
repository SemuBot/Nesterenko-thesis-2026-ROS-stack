import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import numpy as np

class CmdVelMotorDriver(Node):
    def __init__(self):
        super().__init__('cmd_vel_motor_driver')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.listener_callback,
            10)

        # Motor setup
        GPIO.setmode(GPIO.BCM)
        self.pwm_pins = [18, 13, 27]   # Right, Left, Back
        self.dir_pins = [6, 23, 4]     # Right, Left, Back

        self.pwms = []

        for pin in self.pwm_pins:
            GPIO.setup(pin, GPIO.OUT)
            pwm = GPIO.PWM(pin, 1000)
            pwm.start(0)
            self.pwms.append(pwm)

        for pin in self.dir_pins:
            GPIO.setup(pin, GPIO.OUT)

        # Inverse kinematics matrix (same as your code)
        self.matrix = np.array([
            [-0.33,  0.58, 0.33],   # Right motor
            [-0.33, -0.58, 0.33],   # Left motor
            [ 0.67,  0.0,  0.33]    # Back motor
        ])

    def listener_callback(self, msg):
        x = msg.linear.x
        z = msg.angular.z

        direction = np.array([x, 0.0, z])  # no strafing
        result = np.dot(self.matrix, direction)

        for i, vel in enumerate(result):
            duty = min(max(abs(vel * 100), 0), 100)  # Scale to 0–100

            if vel < 0:
                GPIO.output(self.dir_pins[i], GPIO.LOW)
            else:
                GPIO.output(self.dir_pins[i], GPIO.HIGH)

            self.pwms[i].ChangeDutyCycle(duty)

    def destroy_node(self):
        for pwm in self.pwms:
            pwm.stop()
        GPIO.cleanup()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelMotorDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
