#!/usr/bin/env bash
set -euo pipefail

echo "[test_cmd_vel_safe] Publishing a low-speed safe /cmd_vel command..."
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 0.05, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.05}}"

echo "[test_cmd_vel_safe] Done. Check /hardware/cmd_vel_status and /odom topics."
