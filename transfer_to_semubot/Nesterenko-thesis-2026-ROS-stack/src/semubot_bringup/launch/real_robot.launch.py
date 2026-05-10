from launch import LaunchDescription
from launch.actions import LogInfo


# TODO(semubot): Integrate validated real hardware launch sequence only after
# dedicated lab safety sign-off and explicit operator approval.
def generate_launch_description():
    return LaunchDescription([
        LogInfo(
            msg='real_robot.launch.py is intentionally a safety placeholder. '
                'Use mock_robot.launch.py for default operation.'
        )
    ])
