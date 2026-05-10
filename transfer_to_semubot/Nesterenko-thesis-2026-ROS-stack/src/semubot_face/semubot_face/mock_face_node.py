import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockFaceNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_face_node')
        self._sub = self.create_subscription(String, '/face/expression', self._callback, 10)
        self._status_pub = self.create_publisher(String, '/face/status', 10)

    def _callback(self, msg: String) -> None:
        self.get_logger().info(f'Face expression request: {msg.data}')
        self._status_pub.publish(String(data=f'face mock applied expression: {msg.data}'))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockFaceNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
