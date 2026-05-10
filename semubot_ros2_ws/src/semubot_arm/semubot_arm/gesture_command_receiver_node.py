import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class GestureCommandReceiverNode(Node):
    def __init__(self) -> None:
        super().__init__('gesture_command_receiver_node')
        self._sub = self.create_subscription(
            String,
            '/arm/gesture_command',
            self._callback,
            10,
        )
        self._status_pub = self.create_publisher(String, '/arm/status', 10)

    def _callback(self, msg: String) -> None:
        # TODO(semubot): Replace this placeholder with a real serial driver adapter.
        status = f'gesture command accepted in mock path: {msg.data}'
        self.get_logger().info(status)
        self._status_pub.publish(String(data=status))


def main(args=None) -> None:
    rclpy.init(args=args)
    node = GestureCommandReceiverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
