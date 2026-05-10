import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from std_msgs.msg import String


class DemoBehaviorNode(Node):
    def __init__(self) -> None:
        super().__init__('demo_behavior_node')

        self.declare_parameter('enable_motion_demo', False)
        self.declare_parameter('publish_period_sec', 5.0)
        self.declare_parameter('motion_linear_x', 0.03)
        self.declare_parameter('motion_angular_z', 0.05)

        self._state_pub = self.create_publisher(String, '/semubot/demo_state', 10)
        self._face_pub = self.create_publisher(String, '/face/expression', 10)
        self._gesture_pub = self.create_publisher(String, '/arm/gesture_command', 10)
        self._cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        period = float(self.get_parameter('publish_period_sec').value)
        self._timer = self.create_timer(period, self._publish_demo_step)

    def _publish_demo_step(self) -> None:
        self._state_pub.publish(String(data='GREETING'))
        self._face_pub.publish(String(data='smile'))
        self._gesture_pub.publish(String(data='wave'))

        if bool(self.get_parameter('enable_motion_demo').value):
            twist = Twist()
            twist.linear.x = float(self.get_parameter('motion_linear_x').value)
            twist.angular.z = float(self.get_parameter('motion_angular_z').value)
            self._cmd_vel_pub.publish(twist)
            self.get_logger().info('Published low-speed demo /cmd_vel command')
        else:
            self.get_logger().info('Published GREETING behavior without motion')


def main(args=None) -> None:
    rclpy.init(args=args)
    node = DemoBehaviorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
