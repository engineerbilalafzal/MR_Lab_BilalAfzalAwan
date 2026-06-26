import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')
        self.subscription = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, 10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.front_threshold = 0.55
        self.forward_speed = 0.12
        self.turn_speed = 0.55

        self.publish_stop()

    def publish_stop(self):
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.publisher.publish(twist)

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)

        # --- TODO 1: Clean data ---
        ranges = np.where(np.isfinite(ranges), ranges, 3.5)

        # --- TODO 2: Define regions (360-degree scan, index 0 = front) ---
        front = np.concatenate([ranges[0:20], ranges[340:360]])
        left  = ranges[60:120]
        right = ranges[240:300]

        front_dist = float(np.min(front))
        left_dist  = float(np.min(left))
        right_dist = float(np.min(right))

        self.get_logger().info(
            f"front={front_dist:.2f} left={left_dist:.2f} right={right_dist:.2f}")

        twist = Twist()

        if front_dist < self.front_threshold:
            twist.linear.x = 0.0
            if left_dist > right_dist:
                twist.angular.z = self.turn_speed
            else:
                twist.angular.z = -self.turn_speed
        else:
            twist.linear.x = self.forward_speed
            twist.angular.z = 0.0

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    try:
        rclpy.spin(node)
    finally:
        node.publish_stop()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
