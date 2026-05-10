import math

import rclpy
from geometry_msgs.msg import Quaternion, TransformStamped, Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node
from tf2_ros import TransformBroadcaster


class MockBaseHardwareNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_base_hardware')

        self.declare_parameter('max_linear_velocity', 0.10)
        self.declare_parameter('max_angular_velocity', 0.30)
        self.declare_parameter('publish_rate', 20.0)
        self.declare_parameter('enable_motion', True)
        self.declare_parameter('base_frame', 'base_link')
        self.declare_parameter('odom_frame', 'odom')

        self._odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self._cmd_vel_sub = self.create_subscription(Twist, '/cmd_vel', self._cmd_vel_callback, 10)
        self._tf_broadcaster = TransformBroadcaster(self)

        self._x = 0.0
        self._y = 0.0
        self._yaw = 0.0

        self._cmd_linear_x = 0.0
        self._cmd_linear_y = 0.0
        self._cmd_angular_z = 0.0

        self._last_time = self.get_clock().now()
        rate = float(self.get_parameter('publish_rate').value)
        period = 1.0 / rate if rate > 0.0 else 0.05
        self._timer = self.create_timer(period, self._update_and_publish)

        self.get_logger().info(
            'mock_base_hardware_node started in MOCK mode only. '
            'This node publishes simulated /odom and odom->base_link TF and does not control real hardware.'
        )

    def _cmd_vel_callback(self, msg: Twist) -> None:
        max_linear = float(self.get_parameter('max_linear_velocity').value)
        max_angular = float(self.get_parameter('max_angular_velocity').value)

        linear_speed = math.hypot(msg.linear.x, msg.linear.y)
        angular_speed = abs(msg.angular.z)

        if linear_speed > max_linear or angular_speed > max_angular:
            self.get_logger().warning(
                'Ignoring /cmd_vel in mock odometry: linear=%.3f angular=%.3f exceeds limits '
                '(linear<=%.3f angular<=%.3f)'
                % (linear_speed, angular_speed, max_linear, max_angular)
            )
            return

        self._cmd_linear_x = float(msg.linear.x)
        self._cmd_linear_y = float(msg.linear.y)
        self._cmd_angular_z = float(msg.angular.z)

    def _update_and_publish(self) -> None:
        now = self.get_clock().now()
        dt = (now - self._last_time).nanoseconds / 1e9
        if dt <= 0.0:
            return
        self._last_time = now

        if bool(self.get_parameter('enable_motion').value):
            vx_world = (
                self._cmd_linear_x * math.cos(self._yaw)
                - self._cmd_linear_y * math.sin(self._yaw)
            )
            vy_world = (
                self._cmd_linear_x * math.sin(self._yaw)
                + self._cmd_linear_y * math.cos(self._yaw)
            )
            self._x += vx_world * dt
            self._y += vy_world * dt
            self._yaw += self._cmd_angular_z * dt

        self._publish_odom(now)
        self._publish_tf(now)

    def _publish_odom(self, stamp) -> None:
        odom_frame = str(self.get_parameter('odom_frame').value)
        base_frame = str(self.get_parameter('base_frame').value)

        msg = Odometry()
        msg.header.stamp = stamp.to_msg()
        msg.header.frame_id = odom_frame
        msg.child_frame_id = base_frame

        msg.pose.pose.position.x = self._x
        msg.pose.pose.position.y = self._y
        msg.pose.pose.position.z = 0.0
        msg.pose.pose.orientation = self._quaternion_from_yaw(self._yaw)

        msg.twist.twist.linear.x = self._cmd_linear_x
        msg.twist.twist.linear.y = self._cmd_linear_y
        msg.twist.twist.angular.z = self._cmd_angular_z

        self._odom_pub.publish(msg)

    def _publish_tf(self, stamp) -> None:
        odom_frame = str(self.get_parameter('odom_frame').value)
        base_frame = str(self.get_parameter('base_frame').value)

        transform = TransformStamped()
        transform.header.stamp = stamp.to_msg()
        transform.header.frame_id = odom_frame
        transform.child_frame_id = base_frame
        transform.transform.translation.x = self._x
        transform.transform.translation.y = self._y
        transform.transform.translation.z = 0.0
        transform.transform.rotation = self._quaternion_from_yaw(self._yaw)

        self._tf_broadcaster.sendTransform(transform)

    @staticmethod
    def _quaternion_from_yaw(yaw: float) -> Quaternion:
        quat = Quaternion()
        quat.x = 0.0
        quat.y = 0.0
        quat.z = math.sin(yaw * 0.5)
        quat.w = math.cos(yaw * 0.5)
        return quat


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockBaseHardwareNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
