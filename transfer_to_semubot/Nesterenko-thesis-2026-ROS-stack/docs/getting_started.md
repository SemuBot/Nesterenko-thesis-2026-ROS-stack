# Getting Started

This guide is for new students joining the SemuBot ROS 2 stack project.

## 1. Prerequisites

Recommended environment:
- Ubuntu 24.04
- ROS 2 Jazzy

If parts of legacy code were built against ROS 2 Humble, keep compatibility notes in package docs and avoid unnecessary breaking changes.

## 2. Build the workspace

```bash
cd semubot_ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

## 3. Verify package discovery

```bash
ros2 pkg list | grep semubot
```

## 4. Launch core modes

Visualization mode:
```bash
ros2 launch semubot_bringup visualization.launch.py
```

Mock robot mode:
```bash
ros2 launch semubot_bringup mock_robot.launch.py
```

Demo behavior mode:
```bash
ros2 launch semubot_bringup demo_behavior.launch.py
```

## 5. Basic graph checks

```bash
ros2 node list
ros2 topic list
```

Expected baseline topics include `/joint_states`, `/tf`, `/tf_static`, and `/semubot/demo_state` (in demo mode).

## 6. Safe command test

```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.05, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.05}}"
```

`safe_cmd_vel_receiver_node` should log command acceptance/rejection according to configured limits.

## 7. Important safety defaults

- Real robot motion is disabled by default.
- `enable_real_motion=false` is required unless supervised lab testing is explicitly prepared.
- Do not bypass safety wrappers for quick experiments.

## 8. Where to go next

- Architecture details: `docs/architecture.md`
- Full test workflow: `docs/testing_plan.md`
- Lab safety protocol: `docs/lab_test_protocol.md`
- Historical subsystem context: `docs/previous_work.md`
- Media and demos: `docs/demos.md`
