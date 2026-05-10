import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class MockScanNode(Node):
    def __init__(self) -> None:
        super().__init__('mock_scan_node')

        self.declare_parameter('topic_name', '/scan')
        self.declare_parameter('frame_id', 'laser_frame')
        self.declare_parameter('publish_rate_hz', 8.0)
        self.declare_parameter('angle_min', -math.pi)
        self.declare_parameter('angle_max', math.pi)
        self.declare_parameter('num_readings', 360)
        self.declare_parameter('range_min', 0.10)
        self.declare_parameter('range_max', 6.0)

        topic_name = str(self.get_parameter('topic_name').value)
        self._publisher = self.create_publisher(LaserScan, topic_name, 10)

        publish_rate = float(self.get_parameter('publish_rate_hz').value)
        timer_period = 1.0 / publish_rate if publish_rate > 0.0 else 0.125
        self._timer = self.create_timer(timer_period, self._publish_scan)

        self.get_logger().info(
            'mock_scan_node started. Publishing placeholder /scan in an obstacle-free mock environment.'
        )

    def _publish_scan(self) -> None:
        angle_min = float(self.get_parameter('angle_min').value)
        angle_max = float(self.get_parameter('angle_max').value)
        num_readings = int(self.get_parameter('num_readings').value)
        range_min = float(self.get_parameter('range_min').value)
        range_max = float(self.get_parameter('range_max').value)

        if num_readings < 2:
            num_readings = 2

        angle_increment = (angle_max - angle_min) / (num_readings - 1)

        scan = LaserScan()
        scan.header.stamp = self.get_clock().now().to_msg()
        scan.header.frame_id = str(self.get_parameter('frame_id').value)
        scan.angle_min = angle_min
        scan.angle_max = angle_max
        scan.angle_increment = angle_increment
        scan.time_increment = 0.0
        scan.scan_time = 0.0
        scan.range_min = range_min
        scan.range_max = range_max

        # Obstacle-free placeholder distances for Nav2 wiring tests.
        nominal_range = max(range_min, range_max - 0.2)
        scan.ranges = [nominal_range for _ in range(num_readings)]
        scan.intensities = [0.0 for _ in range(num_readings)]

        self._publisher.publish(scan)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MockScanNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
