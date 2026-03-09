#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import os
from pathlib import Path


class CounterNode(Node):
    def __init__(self):
        super().__init__('counter_node')
        
        # Get package directory
        package_dir = Path(__file__).parent.parent
        self.counter_file = package_dir / 'counter.txt'
        
        # Read or initialize counter
        self.counter = self.read_counter()
        self.counter += 1
        self.write_counter(self.counter)
        
        self.get_logger().info(f'Run count: {self.counter}')
    
    def read_counter(self):
        """Read counter from file, return 0 if file doesn't exist"""
        try:
            if self.counter_file.exists():
                with open(self.counter_file, 'r') as f:
                    return int(f.read().strip())
        except Exception as e:
            self.get_logger().warn(f'Error reading counter file: {e}')
        return 0
    
    def write_counter(self, value):
        """Write counter to file"""
        try:
            with open(self.counter_file, 'w') as f:
                f.write(str(value))
        except Exception as e:
            self.get_logger().error(f'Error writing counter file: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
