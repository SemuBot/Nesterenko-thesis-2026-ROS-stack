from launch import LaunchDescription
from launch.actions import LogInfo


def generate_launch_description():
    return LaunchDescription([
        LogInfo(
            msg='Simulation placeholder: use semubot_bringup visualization.launch.py '
                'for RViz-only mode.'
        )
    ])
