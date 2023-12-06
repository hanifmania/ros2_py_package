#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoyButtonListener(Node):
    def __init__(self):
        super().__init__('joy_button_listener')
        self.create_subscription(Joy, 'joy', self.joy_callback, 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.joy_active = False


    def joy_callback(self, msg):
        # Print the received message to debug
        self.get_logger().info('Received Joy message: %s' % str(msg))

        # Check if any button is pressed (1 in msg.buttons indicates a button press)
        if 1 in msg.buttons:
            if not self.joy_active:
                self.get_logger().info('Joy is active')
                self.joy_active = True
        else:
            self.get_logger().info('Joy is inactive')
            self.joy_active = False

    def timer_callback(self):
        self.get_logger().info('Node is active')

def main(args=None):
    rclpy.init(args=args)
    joy_button_listener = JoyButtonListener()
    
    
    try:
        rclpy.spin(joy_button_listener)
    except KeyboardInterrupt:
        pass
    finally:
        joy_button_listener.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()



