# Nav2 Mock Integration (Package-Level)

This document describes the package-level Nav2 mock integration assets in `semubot_navigation`.

## Included files

- `launch/nav2_mock.launch.py`
- `config/nav2_params.yaml`
- `maps/empty_map.yaml`
- `maps/empty_map.pgm`
- `rviz/nav2_mock.rviz`

## Safety note

This integration is mock-only and does not connect Nav2 output to real motors.

## Dependencies

If Nav2 is not installed, install with:

```bash
sudo apt install ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup
```

## Launch entry point

```bash
ros2 launch semubot_navigation nav2_mock.launch.py
```

For top-level usage, prefer:

```bash
ros2 launch semubot_bringup nav2_mock.launch.py
```
