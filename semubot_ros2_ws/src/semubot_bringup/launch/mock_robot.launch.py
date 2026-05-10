from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    enable_safety_receiver_arg = DeclareLaunchArgument(
        'enable_safety_receiver',
        default_value='false',
        description='Enable standalone safe_cmd_vel_receiver_node. Keep false when mock base consumes /cmd_vel.',
    )

    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('semubot_description'),
                'launch',
                'display.launch.py',
            ])
        )
    )

    safe_cmd_vel_receiver = Node(
        package='semubot_hardware',
        executable='safe_cmd_vel_receiver_node',
        output='screen',
        condition=IfCondition(LaunchConfiguration('enable_safety_receiver')),
        parameters=[
            {
                'max_linear_velocity': 0.10,
                'max_angular_velocity': 0.30,
                'enable_real_motion': False,
            }
        ],
    )

    mock_base_hardware = Node(
        package='semubot_hardware',
        executable='mock_base_hardware_node',
        output='screen',
        parameters=[
            {
                'max_linear_velocity': 0.10,
                'max_angular_velocity': 0.30,
                'publish_rate': 20.0,
                'enable_motion': True,
                'base_frame': 'base_link',
                'odom_frame': 'odom',
            }
        ],
    )

    hardware_status = Node(
        package='semubot_hardware',
        executable='hardware_status_node',
        output='screen',
    )

    mock_arm = Node(
        package='semubot_arm',
        executable='mock_arm_node',
        output='screen',
    )

    mock_system_monitor = Node(
        package='semubot_system_monitor',
        executable='mock_system_monitor_node',
        output='screen',
    )

    mock_face = Node(
        package='semubot_face',
        executable='mock_face_node',
        output='screen',
    )

    return LaunchDescription([
        enable_safety_receiver_arg,
        description_launch,
        safe_cmd_vel_receiver,
        mock_base_hardware,
        hardware_status,
        mock_arm,
        mock_system_monitor,
        mock_face,
    ])
