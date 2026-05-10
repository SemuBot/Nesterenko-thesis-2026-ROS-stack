from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    mock_robot_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('semubot_bringup'),
                'launch',
                'mock_robot.launch.py',
            ])
        )
    )

    demo_behavior = Node(
        package='semubot_behavior',
        executable='demo_behavior_node',
        output='screen',
        parameters=[{'enable_motion_demo': False}],
    )

    return LaunchDescription([
        mock_robot_launch,
        demo_behavior,
    ])
