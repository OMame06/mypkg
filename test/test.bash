#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 run mypkg year_count > /tmp/mypkg.log

echo "Checking for year-end results..."
ros2 topic echo /year_count std_msgs/msg/Int16 | grep "100.0000"  # or "残り時間(秒): 0"
if [ $? -eq 0 ]; then
    echo "Success: Year-end reached."
else
    echo "Failed: Year-end check failed."
fi
#[成功例]
#年末のパーセントが100%か、残り時間が0秒か
#年始のパーセントが  0%か、残り時間がMAX秒か
#うるう年にも対応しているか、パーセントと残り時間

#[失敗例]
#打ち間違いによるエラー
