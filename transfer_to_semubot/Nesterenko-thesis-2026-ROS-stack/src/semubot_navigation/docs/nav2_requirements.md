# Nav2 Requirements for SemuBot

## Goal of this phase

This phase prepares SemuBot for future Nav2 integration by validating:

- `/cmd_vel` handling and limits,
- `/odom` quality and consistency,
- dynamic TF (`odom -> base_link`),
- frame naming conventions in URDF and runtime transforms.

## Required upstream inputs before enabling full Nav2

1. Consistent odometry:
   - `/odom` (`nav_msgs/Odometry`)
   - dynamic `odom -> base_link` transform
2. Stable TF tree:
   - at minimum `map`, `odom`, `base_link`, and major sensor frames
3. Obstacle sensing:
   - `/scan` or a depth-to-obstacle pipeline suitable for local planning
4. Localization:
   - AMCL, EKF, or another validated localization source
5. Velocity endpoint:
   - `/cmd_vel` consumer with explicit safety constraints

## Current status

- `semubot_navigation/launch/navigation_mock.launch.py` supports a mock-readiness workflow.
- `semubot_hardware/mock_base_hardware_node.py` provides mock odometry and TF.
- `nav2_bringup` is optional; launch prints a clear message if not installed.

## Why full Nav2 remains future work

Full navigation behavior should not be enabled until:

- real odometry is validated against physical motion,
- obstacle sensing is reliable in lab conditions,
- localization drift is measured and acceptable,
- command limits and emergency handling are verified on hardware.
