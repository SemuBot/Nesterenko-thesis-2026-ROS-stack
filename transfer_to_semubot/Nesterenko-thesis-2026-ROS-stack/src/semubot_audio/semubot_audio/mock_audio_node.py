import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockAudioNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_audio_node')
        self._raw_pub = self.create_publisher(String, '/audio/raw', 10)
        self._doa_pub = self.create_publisher(String, '/audio/doa', 10)
        self._status_pub = self.create_publisher(String, '/audio/status', 10)
        self._timer = self.create_timer(3.0, self._tick)

    def _tick(self) -> None:
        self._raw_pub.publish(String(data='mock audio frame'))
        self._doa_pub.publish(String(data='0.0'))
        self._status_pub.publish(String(data='audio mock active'))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockAudioNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
