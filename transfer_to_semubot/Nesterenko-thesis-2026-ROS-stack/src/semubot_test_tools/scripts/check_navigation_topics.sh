#!/usr/bin/env bash
set -euo pipefail

echo "[check_navigation_topics] Nodes:"
ros2 node list
echo
echo "[check_navigation_topics] Topics:"
ros2 topic list
echo
echo "[check_navigation_topics] Echo /odom (Ctrl+C to stop):"
ros2 topic echo /odom
