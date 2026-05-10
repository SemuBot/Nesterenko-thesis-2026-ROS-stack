# SemuBot ROS 2 Architecture

## 1. Why modular ROS 2 architecture is required

SemuBot development has accumulated subsystem implementations from multiple thesis tracks
(face/neck, audio, speech, vision, arm mechanics, servo control, and mobile base integration).
A modular ROS 2 architecture is required so future students can:

- develop subsystem packages independently,
- test in mock mode before touching hardware,
- replace internal implementations without breaking public topic interfaces,
- maintain a single thesis-grade integration workspace.

## 2. Architectural layers

The stack is organized into the following layers:

1. **Robot description**
   - Package: `semubot_description`
   - URDF/xacro, frames, visualization model, RViz configuration.

2. **Hardware abstraction**
   - Package: `semubot_hardware`
   - Safe command validation, mock hardware nodes, hardware status wrappers.

3. **Control**
   - Package: `semubot_control`
   - Controller configuration placeholders for ros2_control evolution.

4. **Perception**
   - Package: `semubot_vision`
   - Vision topic wrappers and mock vision outputs.

5. **Interaction and behavior**
   - Packages: `semubot_audio`, `semubot_speech`, `semubot_face`, `semubot_behavior`
   - Social interaction channels and high-level behavior coordination.

6. **Navigation**
   - Package: `semubot_navigation`
   - Navigation readiness launch, Nav2 placeholders, and integration requirements.

7. **Manipulation**
   - Packages: `semubot_arm`, `semubot_moveit_config`
   - Gesture-level arm interface now; MoveIt 2 planning integration later.

8. **Simulation and visualization**
   - Package: `semubot_simulation` + visualization launch from bringup/description
   - RViz-first workflow, physics simulation integration planned.

9. **System monitoring**
   - Package: `semubot_system_monitor`
   - Battery/system/diagnostic status in mock and future real mode.

## 3. Package responsibilities and boundaries

- `semubot_bringup` is the orchestration entry point for launch modes.
- `semubot_behavior` should not directly control motor drivers.
- `semubot_hardware` is responsible for safety checks before hardware forwarding.
- `semubot_interfaces` contains custom interfaces only when standard messages are insufficient.
- Real hardware-specific drivers should be isolated behind clear adapters and TODO-gated transitions.

## 4. Data flow (navigation readiness baseline)

1. `semubot_behavior` can publish optional low-speed `/cmd_vel` during demo mode.
2. `safe_cmd_vel_receiver_node` validates `/cmd_vel` and enforces real-motion gate (`enable_real_motion=false` by default).
3. `mock_base_hardware_node` subscribes to `/cmd_vel`, clamps values, and integrates mock planar motion.
4. `mock_base_hardware_node` publishes:
   - `/odom` (`nav_msgs/msg/Odometry`)
   - dynamic TF `odom -> base_link`
5. `robot_state_publisher` + `joint_state_publisher` provide robot model frames for visualization.
6. `semubot_system_monitor` publishes `/system/status`, `/battery_state`, and `/diagnostics`.

## 5. `safe_cmd_vel_receiver_node` vs `mock_base_hardware_node`

Both nodes can subscribe to `/cmd_vel`, but they serve different purposes:

- **safe_cmd_vel_receiver_node**
  - safety gate and audit logger
  - required when evaluating command safety policy
  - does not move hardware by default

- **mock_base_hardware_node**
  - mock mobile base dynamics and odometry publisher
  - used for navigation readiness tests and TF/odom validation

Recommended usage:
- For navigation readiness: run `mock_base_hardware_node`; optionally also run safe receiver for parallel safety logging.
- For pure command safety tests: run safe receiver alone.

## 6. Mapping previous thesis subsystems into this architecture

- Existing URDF/kinematics material -> `semubot_description`
- Existing base driver/control experiments -> `semubot_hardware` and `semubot_control`
- Audio/speech/face experiments -> `semubot_audio`, `semubot_speech`, `semubot_face`
- Arm/servo experiments -> `semubot_arm` + future `semubot_moveit_config`

See `docs/previous_work.md` for subsystem-by-subsystem mapping notes.

## 7. Safety and integration strategy

- Default mode is mock/safe mode.
- Real motion forwarding is disabled by default.
- All uncertain hardware integration points should remain explicitly marked with TODO notes.
- Velocity limits must remain conservative for supervised lab testing.


## 8. Nav2 mock integration status

The stack now includes a mock Nav2 integration launch path (`semubot_bringup/nav2_mock.launch.py`) that provides:
- mock `map -> odom`,
- mock base odometry (`/odom`, `odom -> base_link`),
- mock `/scan`,
- optional Nav2 bringup if installed.

This is an architectural readiness step only; it is not real-robot autonomous navigation.


## 9. Robot Description and Mesh Strategy

- RViz visualization uses real SemuBot meshes sourced from prior SemuBot description assets.
- Collision geometry is intentionally simplified for stable planning/costmap behavior.
- Nav2 uses footprint/radius and collision envelopes, not full decorative mesh detail.
- TF correctness (`map -> odom -> base_link -> sensor frames`) is more critical to navigation than visual mesh detail.
