import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from std_msgs.msg import String


class MockSystemMonitorNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_system_monitor_node')
        self._system_pub = self.create_publisher(String, '/system/status', 10)
        self._diag_pub = self.create_publisher(String, '/diagnostics', 10)
        self._battery_pub = self.create_publisher(BatteryState, '/battery_state', 10)
        self._timer = self.create_timer(2.0, self._publish_status)

    def _publish_status(self) -> None:
        self._system_pub.publish(String(data='SemuBot mock system nominal'))
        self._diag_pub.publish(String(data='diagnostics: mock mode active'))

        battery = BatteryState()
        battery.header.stamp = self.get_clock().now().to_msg()
        battery.voltage = 24.0
        battery.percentage = 0.75
        battery.present = True
        self._battery_pub.publish(battery)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockSystemMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
