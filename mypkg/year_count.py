import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16,Float32
import datetime


#クラス
class Limit(Node):
    def __init__(self):
        super().__init__("year_limit")
        self.pub = self.create_publisher(Int16, "year_limit", 10)
        self.pub_p = self.create_publisher(Float32, "year_percent", 10)
        self.timer = self.create_timer(1.0, self.year_limit)

        self.origin_percent = None


    def calculation(self):
        now  = datetime.datetime.now()
        new  = datetime.datetime(year=now.year,month=1,  day=1,  hour=1,  minute=0,  second=0 )
        last = datetime.datetime(year=now.year,month=12, day=31, hour=23, minute=59, second=59)
        minute_limit =int((last - now).total_seconds())

        difn = (now - new).total_seconds()
        difl = (last - new).total_seconds()
        int_percent = (difn / difl)*100
        return minute_limit,int_percent


    def year_limit(self):
        result = self.calculation()
        limit = result[0]
        percent = result[1]

        msg_limit = Int16()
        msg_limit.data = limit
        self.pub.publish(msg_limit)

        msg_percent = Float32()
        msg_percent.data = percent
        self.pub_p.publish(msg_percent)

        if (self.origin_percent == None) or (abs(self.origin_percent - percent) > 0.0001):
           self.get_logger().info(f"1年の経過パーセンテージ:{percent:.4f}% | 残り時間(秒):{limit}")
           self.origin_percent = percent
        else:
           self.get_logger().info(f"                                | 残り時間(秒):{limit}")

def main():
    rclpy.init()
    node = Limit()
#test.bashで強制終了する際の対処
    try:
       rclpy.spin(node)
    except rclpy.executors.ExternalShutdownException:
       pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
