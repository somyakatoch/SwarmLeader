# follower_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        self.subscriber_ = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)  # Publisher for follower movement
        self.get_logger().info("Follower Node Initialized.")

    def listener_callback(self, msg):
        self.get_logger().info('Following leader: %s' % msg.linear.x)
        # Implement logic for the follower
        follow_msg = Twist()
        follow_msg.linear.x = msg.linear.x  # Follow the same speed
        follow_msg.angular.z = 0.0  # Keep straight, adjust for real following logic
        self.publisher_.publish(follow_msg)

def main():
    rclpy.init()
    follower_node = FollowerNode()
    rclpy.spin(follower_node)
    follower_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
