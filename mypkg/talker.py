import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import datetime


#クラス
#クラス内はみんな家族
class Limit(Node):
    def __init__(self):
        super().__init__("year_limit")
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.timer = self.create_timer(1.0, self.year_limit)


    def calculation(self):
        now  = datetime.datetime.now()
        new  = datetime.datetime(year=now.year,month=1,  day=1,  hour=1,  minute=1,  second=1 )
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
        msg = Int16()
        self.pub.publish(msg)
        self.get_logger().info(f"1年の経過パーセンテージ:{percent:.2f}% | 残り時間(秒):{limit}")


def main():
    rclpy.init()
    node = Limit()
    rclpy.spin(node)
