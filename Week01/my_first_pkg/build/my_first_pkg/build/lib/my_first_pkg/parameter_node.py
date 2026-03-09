#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class ParameterNode(Node):
    def __init__(self):
        super().__init__('parameter_node')
        
        # Declare the student_name parameter
        self.declare_parameter('student_name', 'not_set')
        
        # Get the parameter value
        student_name = self.get_parameter('student_name').value
        
        if student_name == 'not_set':
            self.get_logger().info('student_name not set')
        else:
            self.get_logger().info(f'Hello, {student_name}!')


def main(args=None):
    rclpy.init(args=args)
    node = ParameterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
