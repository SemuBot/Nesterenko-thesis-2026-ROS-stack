# ROS 2 Stack for Social Humanoid Robot SemuBot

## Project Overview
This repository provides a modular ROS 2 stack architecture for **SemuBot**, an open-source social humanoid robot developed at the University of Tartu.

## Thesis Context
Previous SemuBot thesis works developed separate subsystems (face/neck, audio, speech, vision, power, arms, servo control, and initial ROS 2 integration).  
This repository organizes those efforts into a unified ROS 2 stack with clearer package boundaries and safer integration flow.

## Repository Purpose
The repository is intended to provide a maintainable, buildable, and testable architecture for future students and researchers extending SemuBot.

## Architecture Overview
Main architecture layers:
- robot description
- hardware abstraction
- control
- perception
- interaction/behavior
- navigation
- manipulation
- simulation/visualization
- system monitoring

## Robot Description and Mesh Strategy
- The active `semubot_description` now uses **actual SemuBot visual meshes** for RViz visualization.
- Collision geometry remains **simplified** (cylinders/boxes/spheres) for navigation and simulation stability.
- Nav2 behavior depends primarily on TF, odometry, `/cmd_vel`, `/scan`, and footprint/costmap parameters.
- The decorative visual mesh model is intentionally different from the navigation collision model.

## Package Structure
Primary stack lives in `semubot_ros2_ws/src/`:

- `semubot_description`
- `semubot_bringup`
- `semubot_control`
- `semubot_hardware`
- `semubot_interfaces`
- `semubot_behavior`
- `semubot_audio`
- `semubot_vision`
- `semubot_speech`
- `semubot_face`
- `semubot_arm`
- `semubot_navigation`
- `semubot_moveit_config`
- `semubot_simulation`
- `semubot_system_monitor`
- `semubot_test_tools`

## Requirements
- Ubuntu 24.04 (recommended)
- ROS 2 Jazzy (recommended target)
- Note: some legacy subsystem code was originally developed for ROS 2 Humble. Keep compatibility notes when reusing older components.

## Installation
```bash
cd semubot_ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

## Build Instructions
```bash
cd semubot_ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

## Launch Instructions
```bash
ros2 launch semubot_bringup visualization.launch.py
ros2 launch semubot_bringup mock_robot.launch.py
ros2 launch semubot_bringup navigation_readiness.launch.py
ros2 launch semubot_bringup demo_behavior.launch.py
```


## Mock Nav2 Integration
Use mock Nav2 mode to validate architecture readiness without controlling the real robot:

```bash
ros2 launch semubot_bringup nav2_mock.launch.py
```

This mode is safe by default and routes `/cmd_vel` through mock/safe nodes only.
See: `semubot_ros2_ws/docs/nav2_mock_integration.md`.

## Basic Testing Commands
```bash
ros2 node list
ros2 topic list
ros2 topic echo /joint_states
ros2 topic echo /odom
ros2 topic echo /semubot/demo_state
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.05, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.05}}"
```

## Safe `/cmd_vel` Test
`semubot_hardware/safe_cmd_vel_receiver_node` validates velocity limits and rejects unsafe commands before any real hardware forwarding.

`semubot_hardware/mock_base_hardware_node` is used for navigation readiness: it consumes `/cmd_vel`, publishes mock `/odom`, and broadcasts dynamic `odom -> base_link` TF.

Default safety parameters:
- `max_linear_velocity = 0.10`
- `max_angular_velocity = 0.30`
- `enable_real_motion = false`

## Real Robot Safety Warning
Real robot motion is disabled by default and must only be tested under supervised lab conditions with:
- low velocity limits,
- emergency power access,
- sufficient free space,
- one nearby safety observer.

See full protocol: `semubot_ros2_ws/docs/lab_test_protocol.md`.

## Documentation Links
- Getting started: `semubot_ros2_ws/docs/getting_started.md`
- Architecture: `semubot_ros2_ws/docs/architecture.md`
- Navigation readiness: `semubot_ros2_ws/docs/navigation_readiness.md`
- Testing plan: `semubot_ros2_ws/docs/testing_plan.md`
- Lab safety protocol: `semubot_ros2_ws/docs/lab_test_protocol.md`
- Previous subsystem context: `semubot_ros2_ws/docs/previous_work.md`
- Demos and media index: `semubot_ros2_ws/docs/demos.md`
- Future roadmap: `semubot_ros2_ws/docs/future_work.md`
- Media policy: `semubot_ros2_ws/media/README.md`

## Future Work
Near-term priorities:
- validate real odometry sources and obstacle sensing for Nav2,
- integrate validated hardware drivers behind safety wrappers,
- migrate mock nodes to production subsystem integrations,
- stage Nav2 and MoveIt 2 onboarding,
- expand automated test and CI coverage.

## Contribution Guidelines for Future Students
1. Keep package responsibilities clear and documented.
2. Prefer standard ROS 2 messages unless custom interfaces are necessary.
3. Keep real motion disabled by default in new code paths.
4. Add launch and test instructions with every subsystem change.
5. Place large media in `semubot_ros2_ws/media/` and reference it from `docs/demos.md` (do not overload this root README).
