import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MockVisionNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_vision_node')
        self._image_pub = self.create_publisher(String, '/camera/image_raw', 10)
        self._faces_pub = self.create_publisher(String, '/vision/faces', 10)
        self._gaze_pub = self.create_publisher(String, '/vision/gaze_target', 10)
        self._emotion_pub = self.create_publisher(String, '/vision/person_emotion', 10)
        self._identity_pub = self.create_publisher(String, '/vision/person_identity', 10)
        self._status_pub = self.create_publisher(String, '/vision/status', 10)
        self._timer = self.create_timer(2.0, self._tick)

    def _tick(self) -> None:
        self._image_pub.publish(String(data='mock_image_frame'))
        self._faces_pub.publish(String(data='[]'))
        self._gaze_pub.publish(String(data='none'))
        self._emotion_pub.publish(String(data='unknown'))
        self._identity_pub.publish(String(data='unknown'))
        self._status_pub.publish(String(data='vision mock active'))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockVisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
