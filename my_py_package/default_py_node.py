import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class DefaultPyNode(Node):
    
    def __init__(self):
        super().__init__('default_py_node')
        self.publisher1 = self.create_publisher(String, 'topic1', 10)
        self.publisher2 = self.create_publisher(String, 'topic2', 10)
        self.subscription1 = self.create_subscription(String, 'topic1', self.listener1_callback, 10)
        self.subscription2 = self.create_subscription(String, 'topic2', self.listener2_callback, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i1 = 0
        self.i2 = 0

    def listener1_callback(self, msg):
        self.get_logger().info('I receive: "%s"' % msg.data)
        self.get_logger().info('Do callback 1...')

    def listener2_callback(self, msg):
        self.get_logger().info('I receive: "%s"' % msg.data)
        self.get_logger().info('Do callback 2...')

    def timer_callback(self):
        msg1 = String()
        msg1.data = 'Hello, topic1! %d' % self.i1
        self.publisher1.publish(msg1)
        self.i1 += 1

        msg2 = String()
        msg2.data = 'Hello, topic2! %d' % self.i2
        self.publisher2.publish(msg2)
        self.i2 += 1

def main(args=None):
    rclpy.init(args=args)

    default_py_node = DefaultPyNode()

    rclpy.spin(default_py_node)

    default_py_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
