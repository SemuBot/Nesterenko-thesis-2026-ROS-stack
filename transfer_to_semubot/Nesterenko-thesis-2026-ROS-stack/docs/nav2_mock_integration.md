# Nav2 Mock Integration

This document describes the PHASE 3 mock Nav2 integration for SemuBot.

## Scope and safety

- This is **mock integration only** for architecture validation.
- Real robot motion remains disabled by default.
- `/cmd_vel` from Nav2 is consumed only by safe/mock nodes in this phase.
- No direct real motor control path is enabled.

## Why Nav2 needs map, TF, odometry, scan, and cmd_vel

Nav2 depends on a consistent navigation data chain:

- `/map` and map server
- TF: `map -> odom -> base_link -> sensor frames`
- `/odom` for short-term motion estimation
- `/scan` (or equivalent obstacle source) for local costmaps
- `/cmd_vel` for velocity command output

If any of these are missing or inconsistent, planning and control behavior is unreliable.

## What is mocked in this phase

- `map -> odom` via static transform publisher
- base odometry via `mock_base_hardware_node`
- laser scan via `mock_scan_node` (`/scan`)
- map asset via `empty_map.yaml` / `empty_map.pgm`

## Launching mock Nav2 integration

```bash
cd semubot_ros2_ws
source install/setup.bash
ros2 launch semubot_bringup nav2_mock.launch.py
```

If Nav2 is not installed:

```bash
sudo apt install ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup
```

## Sending a goal in RViz2

1. Launch `nav2_mock.launch.py`.
2. In RViz2 (`nav2_mock.rviz`), set initial pose (if needed).
3. Use **2D Goal Pose** to send a goal in map frame.
4. Observe planning/control topics and `/cmd_vel`.

## Thesis evidence to collect

- Launch terminal logs
- `ros2 node list`
- `ros2 topic list`
- `/odom`, `/scan`, `/cmd_vel` topic snapshots
- TF graph (`ros2 run tf2_tools view_frames`)
- RViz screenshots of map, robot, scan, and goal markers
- Short video of mock goal workflow

## Before real-robot Nav2

Required next validation steps:

- real odometry quality (encoder/IMU fusion),
- real obstacle sensing quality and latency,
- footprint and controller tuning on hardware,
- supervised low-speed tests with strict lab safety protocol.


## Robot Description and Mesh Strategy

- Visual model: actual SemuBot meshes for realistic RViz appearance.
- Collision model: simplified primitives for robust costmap and planner behavior.
- Nav2 integration uses TF/odom/scan/footprint consistency rather than heavy visual mesh collision.
