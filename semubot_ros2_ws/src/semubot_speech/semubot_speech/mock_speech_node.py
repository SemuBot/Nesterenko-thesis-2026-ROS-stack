import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockSpeechNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_speech_node')
        self._speech_text_pub = self.create_publisher(String, '/speech/text', 10)
        self._dialogue_pub = self.create_publisher(String, '/dialogue/response_text', 10)
        self._audio_out_pub = self.create_publisher(String, '/speech/audio_out', 10)
        self._status_pub = self.create_publisher(String, '/speech/status', 10)
        self._timer = self.create_timer(4.0, self._tick)

    def _tick(self) -> None:
        self._speech_text_pub.publish(String(data='hello semubot'))
        self._dialogue_pub.publish(String(data='Hello, I am in mock speech mode.'))
        self._audio_out_pub.publish(String(data='mock_tts_chunk'))
        self._status_pub.publish(String(data='speech mock active'))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockSpeechNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
