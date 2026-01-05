#!/usr/bin/env python3
import rclpy #type: ignore
from rclpy.node import Node #type: ignore
from turtlesim.msg import Pose #type: ignore

class PoseSubscriber(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose",self.pose_callback,10)

    def pose_callback(self, msg: Pose):
        self.get_logger().info(f'({msg.x}, {msg.y}, {msg.theta})')


def main(args=None):
    rclpy.init(args=args)

    node = PoseSubscriber()
    rclpy.spin(node)

    rclpy.shutdown()