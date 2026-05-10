from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    enable_test_publisher_arg = DeclareLaunchArgument(
        'enable_test_publisher',
        default_value='false',
        description='Publish one low-speed cmd_vel test message from a helper node.',
    )

    max_linear_velocity_arg = DeclareLaunchArgument(
        'max_linear_velocity',
        default_value='0.10',
        description='Safety linear velocity limit for base test.',
    )

    max_angular_velocity_arg = DeclareLaunchArgument(
        'max_angular_velocity',
        default_value='0.30',
        description='Safety angular velocity limit for base test.',
    )

    return LaunchDescription([
        enable_test_publisher_arg,
        max_linear_velocity_arg,
        max_angular_velocity_arg,
        Node(
            package='semubot_hardware',
            executable='safe_cmd_vel_receiver_node',
            output='screen',
            parameters=[
                {
                    'max_linear_velocity': LaunchConfiguration('max_linear_velocity'),
                    'max_angular_velocity': LaunchConfiguration('max_angular_velocity'),
                    'enable_real_motion': False,
                }
            ],
        ),
        Node(
            package='semubot_hardware',
            executable='mock_base_hardware_node',
            output='screen',
            parameters=[
                {
                    'max_linear_velocity': LaunchConfiguration('max_linear_velocity'),
                    'max_angular_velocity': LaunchConfiguration('max_angular_velocity'),
                    'publish_rate': 20.0,
                    'enable_motion': True,
                    'base_frame': 'base_link',
                    'odom_frame': 'odom',
                }
            ],
        ),
        Node(
            package='semubot_behavior',
            executable='demo_behavior_node',
            output='screen',
            parameters=[
                {
                    'enable_motion_demo': True,
                    'motion_linear_x': 0.03,
                    'motion_angular_z': 0.04,
                    'publish_period_sec': 2.0,
                }
            ],
            condition=IfCondition(LaunchConfiguration('enable_test_publisher')),
        ),
    ])
