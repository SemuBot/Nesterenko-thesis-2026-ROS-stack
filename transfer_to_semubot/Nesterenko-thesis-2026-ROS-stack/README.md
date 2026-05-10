# semubot_ros2_ws (workspace guide)

This README is package/workspace-specific.

For the main repository entry point shown on GitHub, use:
- [`../README.md`](../README.md)

## Purpose of this workspace folder

`semubot_ros2_ws/` contains the modular ROS 2 stack packages, launch files, and thesis-oriented documentation.

## Quick build and launch

```bash
cd semubot_ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build
source install/setup.bash

ros2 launch semubot_bringup visualization.launch.py
```

## Detailed docs

- `docs/getting_started.md`
- `docs/architecture.md`
- `docs/testing_plan.md`
- `docs/lab_test_protocol.md`
- `docs/previous_work.md`
- `docs/demos.md`
- `docs/future_work.md`
- `media/README.md`
