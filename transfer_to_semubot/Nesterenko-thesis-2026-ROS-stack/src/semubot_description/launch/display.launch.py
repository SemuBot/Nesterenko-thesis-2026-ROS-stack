from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    use_rviz_arg = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Start RViz with the robot model',
    )
    use_joint_state_publisher_arg = DeclareLaunchArgument(
        'use_joint_state_publisher',
        default_value='true',
        description='Enable joint state publisher path for visualization.',
    )
    use_joint_state_gui_arg = DeclareLaunchArgument(
        'use_joint_state_gui',
        default_value='false',
        description='Use joint_state_publisher_gui instead of joint_state_publisher.',
    )

    xacro_path = PathJoinSubstitution(
        [FindPackageShare('semubot_description'), 'urdf', 'semubot.urdf.xacro']
    )
    rviz_path = PathJoinSubstitution(
        [FindPackageShare('semubot_description'), 'rviz', 'semubot.rviz']
    )

    robot_description = {
        'robot_description': Command(
            [PathJoinSubstitution([FindExecutable(name='xacro')]), ' ', xacro_path]
        )
    }

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description],
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen',
        parameters=[robot_description],
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration('use_joint_state_publisher'),
                    "' == 'true' and '",
                    LaunchConfiguration('use_joint_state_gui'),
                    "' != 'true'",
                ]
            )
        ),
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
        parameters=[robot_description],
        condition=IfCondition(
            PythonExpression(
                [
                    "'",
                    LaunchConfiguration('use_joint_state_publisher'),
                    "' == 'true' and '",
                    LaunchConfiguration('use_joint_state_gui'),
                    "' == 'true'",
                ]
            )
        ),
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_path],
        output='screen',
        condition=IfCondition(LaunchConfiguration('use_rviz')),
    )

    return LaunchDescription(
        [
            use_rviz_arg,
            use_joint_state_publisher_arg,
            use_joint_state_gui_arg,
            robot_state_publisher,
            joint_state_publisher,
            joint_state_publisher_gui,
            rviz2,
        ]
    )
