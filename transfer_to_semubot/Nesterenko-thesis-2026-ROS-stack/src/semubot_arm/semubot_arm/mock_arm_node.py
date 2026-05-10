import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import String


class MockArmNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_arm_node')

        self._gesture_sub = self.create_subscription(
            String,
            '/arm/gesture_command',
            self._gesture_callback,
            10,
        )
        self._status_pub = self.create_publisher(String, '/arm/status', 10)
        self._joint_pub = self.create_publisher(JointState, '/joint_states', 10)

        self._timer = self.create_timer(1.0, self._publish_joint_states)
        self._phase = 0.0

    def _gesture_callback(self, msg: String) -> None:
        self.get_logger().info(f'Received gesture command: {msg.data}')
        self._status_pub.publish(String(data=f'mock arm received gesture: {msg.data}'))

    def _publish_joint_states(self) -> None:
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = ['left_arm_joint', 'right_arm_joint', 'head_yaw_joint']
        joint_state.position = [0.1, -0.1, 0.0]
        joint_state.velocity = [0.0, 0.0, 0.0]
        self._joint_pub.publish(joint_state)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockArmNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
