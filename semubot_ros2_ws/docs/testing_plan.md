# SemuBot Testing Plan

This test plan is designed for thesis evidence collection and repeatable student handover.

## 1) Build and environment setup

```bash
cd semubot_ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash
```

## 2) Package discovery

```bash
ros2 pkg list | grep semubot
```

## 3) Launch navigation readiness stack

```bash
ros2 launch semubot_bringup navigation_readiness.launch.py
```

## 4) Launch base test stack

```bash
ros2 launch semubot_bringup base_test.launch.py
```

Optional command safety logger in the same launch:
```bash
ros2 launch semubot_bringup base_test.launch.py enable_safe_receiver:=true
```

## 5) Inspect ROS graph and core navigation topics

```bash
ros2 node list
ros2 topic list
ros2 topic echo /odom
ros2 topic echo /joint_states
```

## 6) Safe `/cmd_vel` injection test

```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.05, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.05}}"
```

Expected behavior:
- `/cmd_vel` remains within configured limits.
- mock base integrates motion and publishes `/odom`.
- dynamic TF `odom -> base_link` is published.
- no real motor control is executed in default configuration.

## 7) TF validation

```bash
ros2 topic echo /tf
ros2 topic echo /tf_static
ros2 run tf2_tools view_frames
```

## 8) Scripted checks

```bash
./src/semubot_test_tools/scripts/check_navigation_topics.sh
./src/semubot_test_tools/scripts/check_tf_tree.sh
./src/semubot_test_tools/scripts/test_cmd_vel_safe.sh
```

## 9) Supervised real robot low-speed test (future phase)

Perform only after hardware interface validation and safety checklist completion:
- set conservative velocity limits,
- confirm emergency power access,
- test one command at a time,
- keep one operator close to the robot.

## 10) Evidence to collect for thesis reporting

- Terminal logs
- `ros2 node list`
- `ros2 topic list`
- `rqt_graph` screenshot
- RViz screenshot
- Short test video

Store media under `media/` and index it in `docs/demos.md`.


## 11) Nav2 mock integration checks

```bash
ros2 launch semubot_bringup nav2_mock.launch.py
ros2 node list
ros2 topic list
ros2 topic echo /odom
ros2 topic echo /scan
ros2 topic echo /cmd_vel
ros2 run tf2_tools view_frames
```

Verify TF chain includes `map -> odom -> base_link` and sensor frames (e.g., `laser_frame`).


## 12) Mesh and model validation in RViz

During visualization and Nav2 mock launch, verify:
- robot appears as SemuBot mesh model (not stick-like placeholders),
- no "mesh not found" errors in terminal logs,
- TF frames remain valid while mesh model is loaded.
