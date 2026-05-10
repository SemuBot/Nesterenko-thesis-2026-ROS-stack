import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HardwareStatusNode(Node):
    def __init__(self) -> None:
        super().__init__('hardware_status_node')
        self._pub = self.create_publisher(String, '/hardware/status', 10)
        self._timer = self.create_timer(2.0, self._publish_status)

    def _publish_status(self) -> None:
        msg = String()
        msg.data = 'hardware abstraction running in safe mock mode'
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = HardwareStatusNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
