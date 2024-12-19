import rclpy
from rclpy.node import Node
from person_msgs.msg import Person


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)


def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)
