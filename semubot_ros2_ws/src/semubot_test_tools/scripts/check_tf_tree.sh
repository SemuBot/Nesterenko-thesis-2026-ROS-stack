#!/usr/bin/env bash
set -euo pipefail

echo "[check_tf_tree] Listing nodes"
ros2 node list

echo "[check_tf_tree] Listing topics"
ros2 topic list

echo "[check_tf_tree] Inspecting /tf_static (single message)"
timeout 5 ros2 topic echo --once /tf_static || true

echo "[check_tf_tree] Inspecting /tf (single message)"
timeout 5 ros2 topic echo --once /tf || true

echo "[check_tf_tree] Attempting tf2_tools frame graph export"
if ros2 pkg executables tf2_tools >/dev/null 2>&1; then
  ros2 run tf2_tools view_frames || true
else
  echo "tf2_tools is not installed. Install ros-\$ROS_DISTRO-tf2-tools to enable frame graph output."
fi
