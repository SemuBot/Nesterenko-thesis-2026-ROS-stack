import os

from ament_index_python.packages import PackageNotFoundError, get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo, OpaqueFunction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def _maybe_launch_nav2(context):
    if LaunchConfiguration('use_nav2').perform(context).lower() != 'true':
        return []

    nav2_params = LaunchConfiguration('nav2_params').perform(context)
    map_path = LaunchConfiguration('map').perform(context)

    try:
        nav2_share = get_package_share_directory('nav2_bringup')
    except PackageNotFoundError:
        return [
            LogInfo(
                msg=(
                    'nav2_bringup is not installed. Install it with: '
                    'sudo apt install ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup'
                )
            )
        ]

    map_server_param_file = os.path.join(nav2_share, 'params', 'nav2_params.yaml')

    return [
        LogInfo(msg='Launching Nav2 in mock integration mode (no real motor control).'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nav2_share, 'launch', 'bringup_launch.py')),
            launch_arguments={
                'params_file': nav2_params,
                'map': map_path,
                'map_server_params_file': map_server_param_file,
                'autostart': 'false',
                'use_sim_time': 'false',
            }.items(),
        ),
    ]


def generate_launch_description():
    use_nav2_arg = DeclareLaunchArgument(
        'use_nav2',
        default_value='true',
        description='Start Nav2 via nav2_bringup when available.',
    )
    use_rviz_arg = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Start RViz2 with nav2_mock.rviz.',
    )
    launch_mock_base_arg = DeclareLaunchArgument(
        'launch_mock_base',
        default_value='true',
        description='Launch mock_base_hardware_node from this launch file.',
    )
    launch_mock_scan_arg = DeclareLaunchArgument(
        'launch_mock_scan',
        default_value='true',
        description='Launch mock_scan_node to publish placeholder /scan.',
    )
    launch_map_to_odom_arg = DeclareLaunchArgument(
        'launch_map_to_odom',
        default_value='true',
        description='Launch static map->odom transform for mock localization.',
    )
    map_arg = DeclareLaunchArgument(
        'map',
        default_value=PathJoinSubstitution(
            [FindPackageShare('semubot_navigation'), 'maps', 'empty_map.yaml']
        ),
        description='Map yaml file used by mock Nav2 integration.',
    )
    nav2_params_arg = DeclareLaunchArgument(
        'nav2_params',
        default_value=PathJoinSubstitution(
            [FindPackageShare('semubot_navigation'), 'config', 'nav2_params.yaml']
        ),
        description='Nav2 parameter file for mock integration.',
    )

    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare('semubot_description'), 'launch', 'display.launch.py']
            )
        ),
        launch_arguments={'use_rviz': 'false'}.items(),
    )

    mock_base = Node(
        package='semubot_hardware',
        executable='mock_base_hardware_node',
        output='screen',
        condition=IfCondition(LaunchConfiguration('launch_mock_base')),
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

    safe_receiver = Node(
        package='semubot_hardware',
        executable='safe_cmd_vel_receiver_node',
        output='screen',
        parameters=[
            {
                'max_linear_velocity': 0.10,
                'max_angular_velocity': 0.30,
                'enable_real_motion': False,
            }
        ],
    )

    map_to_odom = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        condition=IfCondition(LaunchConfiguration('launch_map_to_odom')),
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
    )

    mock_scan = Node(
        package='semubot_hardware',
        executable='mock_scan_node',
        output='screen',
        condition=IfCondition(LaunchConfiguration('launch_mock_scan')),
        parameters=[
            {
                'topic_name': '/scan',
                'frame_id': 'laser_frame',
                'publish_rate_hz': 8.0,
                'range_min': 0.10,
                'range_max': 6.0,
                'num_readings': 360,
            }
        ],
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        condition=IfCondition(LaunchConfiguration('use_rviz')),
        arguments=[
            '-d',
            PathJoinSubstitution([FindPackageShare('semubot_navigation'), 'rviz', 'nav2_mock.rviz']),
        ],
    )

    info = LogInfo(
        msg=(
            'Starting mock Nav2 integration for SemuBot. '
            'This mode is safe-by-default and does not control real motors.'
        )
    )

    return LaunchDescription(
        [
            use_nav2_arg,
            use_rviz_arg,
            launch_mock_base_arg,
            launch_mock_scan_arg,
            launch_map_to_odom_arg,
            map_arg,
            nav2_params_arg,
            info,
            description_launch,
            mock_base,
            safe_receiver,
            map_to_odom,
            mock_scan,
            rviz,
            OpaqueFunction(function=_maybe_launch_nav2),
        ]
    )
