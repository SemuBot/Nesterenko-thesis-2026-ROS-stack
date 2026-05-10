from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("semubot_description"),
                    "launch",
                    "display.launch.py",
                ]
            )
        ),
        launch_arguments={"use_rviz": "false"}.items(),
    )

    mock_base = Node(
        package="semubot_hardware",
        executable="mock_base_hardware_node",
        output="screen",
        parameters=[
            {
                "max_linear_velocity": 0.10,
                "max_angular_velocity": 0.30,
                "publish_rate": 20.0,
                "enable_motion": True,
                "base_frame": "base_link",
                "odom_frame": "odom",
            }
        ],
    )

    safe_receiver = Node(
        package="semubot_hardware",
        executable="safe_cmd_vel_receiver_node",
        output="screen",
        parameters=[
            {
                "max_linear_velocity": 0.10,
                "max_angular_velocity": 0.30,
                "enable_real_motion": False,
            }
        ],
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=[
            "-d",
            PathJoinSubstitution(
                [FindPackageShare("semubot_description"), "rviz", "semubot.rviz"]
            ),
        ],
    )

    return LaunchDescription(
        [
            description_launch,
            mock_base,
            safe_receiver,
            rviz,
        ]
    )
