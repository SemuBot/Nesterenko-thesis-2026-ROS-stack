from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, LogInfo, OpaqueFunction
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import PackageNotFoundError, get_package_share_directory


def _maybe_launch_nav2(context):
    if LaunchConfiguration("use_nav2").perform(context).lower() != "true":
        return []

    map_path = LaunchConfiguration("map").perform(context)
    nav2_params = LaunchConfiguration("nav2_params").perform(context)

    try:
        nav2_share = get_package_share_directory("nav2_bringup")
    except PackageNotFoundError:
        return [
            LogInfo(
                msg=(
                    "use_nav2:=true was requested, but nav2_bringup is not installed. "
                    "Continuing in navigation-readiness mock mode without Nav2."
                )
            )
        ]

    return [
        LogInfo(
            msg=(
                "Launching nav2_bringup in mock readiness mode. "
                "Validate params/map before real robot usage."
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_share, "/launch/bringup_launch.py"]),
            launch_arguments={
                "params_file": nav2_params,
                "map": map_path,
            }.items(),
        ),
    ]


def generate_launch_description():
    use_rviz_arg = DeclareLaunchArgument(
        "use_rviz",
        default_value="true",
        description="Start RViz from semubot_description display launch",
    )
    use_nav2_arg = DeclareLaunchArgument(
        "use_nav2",
        default_value="false",
        description="Attempt to start nav2_bringup if installed",
    )
    map_file_arg = DeclareLaunchArgument(
        "map",
        default_value=PathJoinSubstitution(
            [FindPackageShare("semubot_navigation"), "maps", "placeholder.yaml"]
        ),
        description="Map yaml path for Nav2 (placeholder by default)",
    )
    nav2_params_arg = DeclareLaunchArgument(
        "nav2_params",
        default_value=PathJoinSubstitution(
            [FindPackageShare("semubot_navigation"), "config", "nav2_params.yaml"]
        ),
        description="Nav2 params yaml path",
    )

    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [FindPackageShare("semubot_description"), "launch", "display.launch.py"]
            )
        ),
        launch_arguments={"use_rviz": LaunchConfiguration("use_rviz")}.items(),
    )

    mock_base_hardware = Node(
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

    nav2_info = LogInfo(
        condition=IfCondition(LaunchConfiguration("use_nav2")),
        msg=(
            "Nav2 bringup requested. If nav2_bringup is unavailable, "
            "the launch will continue in mock mode and print a clear message."
        ),
    )

    base_info = LogInfo(
        msg=(
            "navigation_mock.launch.py started in mock mode. "
            "This launch publishes mock /odom and dynamic odom->base_link TF. "
            "No real hardware control is performed."
        )
    )

    return LaunchDescription(
        [
            use_rviz_arg,
            use_nav2_arg,
            map_file_arg,
            nav2_params_arg,
            base_info,
            description_launch,
            mock_base_hardware,
            nav2_info,
            OpaqueFunction(function=_maybe_launch_nav2),
        ]
    )
