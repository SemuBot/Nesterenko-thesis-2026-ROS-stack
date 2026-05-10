import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from std_msgs.msg import String


class SafeCmdVelReceiverNode(Node):
    def __init__(self) -> None:
        super().__init__('safe_cmd_vel_receiver')

        self.declare_parameter('max_linear_velocity', 0.10)
        self.declare_parameter('max_angular_velocity', 0.30)
        self.declare_parameter('enable_real_motion', False)

        self._status_pub = self.create_publisher(String, '/hardware/cmd_vel_status', 10)
        self._sub = self.create_subscription(Twist, '/cmd_vel', self._cmd_vel_callback, 10)

        self.get_logger().info(
            'safe_cmd_vel_receiver started with limits linear=%.2f m/s angular=%.2f rad/s '
            '(enable_real_motion=%s)'
            % (
                self.get_parameter('max_linear_velocity').value,
                self.get_parameter('max_angular_velocity').value,
                self.get_parameter('enable_real_motion').value,
            )
        )
        self.get_logger().info(
            'Use mock_base_hardware_node for mock odometry and odom->base_link TF publishing. '
            'This node only validates/logs /cmd_vel unless real forwarding is explicitly enabled.'
        )

    def _cmd_vel_callback(self, msg: Twist) -> None:
        max_linear = float(self.get_parameter('max_linear_velocity').value)
        max_angular = float(self.get_parameter('max_angular_velocity').value)
        enable_real_motion = bool(self.get_parameter('enable_real_motion').value)

        linear_speed = math.sqrt(msg.linear.x ** 2 + msg.linear.y ** 2)
        angular_speed = abs(msg.angular.z)

        if linear_speed > max_linear or angular_speed > max_angular:
            warning = (
                'Rejected /cmd_vel: linear=%.3f angular=%.3f exceeds limits '
                '(linear<=%.3f angular<=%.3f)'
                % (linear_speed, angular_speed, max_linear, max_angular)
            )
            self.get_logger().warning(warning)
            self._status_pub.publish(String(data=warning))
            return

        if not enable_real_motion:
            accepted = (
                'Accepted /cmd_vel in MOCK mode: x=%.3f y=%.3f z_ang=%.3f '
                '(no real motor output)'
                % (msg.linear.x, msg.linear.y, msg.angular.z)
            )
            self.get_logger().info(accepted)
            self._status_pub.publish(String(data=accepted))
            return

        # TODO(semubot): Forward validated cmd_vel to real motor driver interface.
        accepted_real = (
            'Accepted /cmd_vel for real motion forwarding: x=%.3f y=%.3f z_ang=%.3f'
            % (msg.linear.x, msg.linear.y, msg.angular.z)
        )
        self.get_logger().info(accepted_real)
        self._status_pub.publish(String(data=accepted_real))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = SafeCmdVelReceiverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
