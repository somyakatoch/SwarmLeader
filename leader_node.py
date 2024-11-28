# leader_node.py
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class LeaderNode(Node):
    def __init__(self):
        super().__init__('leader_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)  # Publisher for movement commands
        self.timer = self.create_timer(1.0, self.timer_callback)  # Timer to send movement commands at regular intervals

    def timer_callback(self):
        msg = Twist()
        # Move forward
        msg.linear.x = 0.5
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.linear.x)

def main():
    rclpy.init()
    leader_node = LeaderNode()
    rclpy.spin(leader_node)
    leader_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
