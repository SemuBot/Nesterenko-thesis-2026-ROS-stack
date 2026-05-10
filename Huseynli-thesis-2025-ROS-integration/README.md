# Semubot ROS2 Integration

This project implements a modular ROS2-based framework for controlling **Semubot**, the first open-source humanoid robot developed in Estonia. The system is split between a laptop (for visualization and control) and a Raspberry Pi 4B (for hardware motor control).

## Project Objectives

- Build a URDF model of Semubot using STL files.
- Visualize the robot in RViz2.
- Implement robot movement using ROS2 `/cmd_vel` topic.
- Deploy ROS2 nodes on Raspberry Pi to control real motors via GPIO.

## ROS2 Workspaces

### 1. `semubot_ros2_ws` (Laptop)
Includes:
- RViz2 visualization
- URDF robot model
- `/cmd_vel` publishing
- Motion simulation logic

### 2. `semubot_raspberry_ws` (Raspberry Pi 4B)
Includes:
- Motor control node
- GPIO command conversion

## Installation Guide

### 1. Install ROS2 Jazzy
Follow the official guide:  
https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

Once installed, source ROS2:
```bash
source /opt/ros/jazzy/setup.bash
```

### 2. Clone Workspaces

#### On Laptop:
```bash
git clone https://github.com/SemuBot/Huseynli-thesis-2025-ROS-integration.git
cd semubot_ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

#### On Raspberry Pi:
```bash
git clone https://github.com/SemuBot/Huseynli-thesis-2025-ROS-integration.git
cd semubot_raspberry_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## Running the System

### On Laptop:
```bash
ros2 launch semubot display_robot.launch.py
```

### On Raspberry Pi:
```bash
ros2 run semubot_motor cmd_vel_motor_driver.py
```

## ROS2 Networking

Ensure both the laptop and Raspberry Pi are on the **same subnet** (LAN). No ROS master is required as ROS2 uses DDS discovery protocol.

To verify connectivity:
```bash
ros2 topic list
```
You should see `/cmd_vel` on both devices.

## Topics Overview

| Topic            | Type                      | Description                        |
|------------------|---------------------------|------------------------------------|
| `/cmd_vel`       | `geometry_msgs/Twist`     | Velocity commands                  |
| `/joint_states`  | `sensor_msgs/JointState`  | Simulated joint data               |
| `/tf`            | `tf2_msgs/TFMessage`      | Transform frames                   |
| `/odom`          | `nav_msgs/Odometry`       | Odometry (simulated)               |

## Author

Omar Huseynli  
University of Tartu – Robotics & Bioengineering  
Email: omar.2005.22.04@gmail.com
