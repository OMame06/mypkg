import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

#講義内で使用
#課題02では使用する必要無し

def generate_launch_description():

    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker',
        )
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([talker,listener])
