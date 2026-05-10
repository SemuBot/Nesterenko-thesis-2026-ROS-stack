# Future Work

This roadmap supports staged thesis development from mock-first integration to supervised real robot validation.

## 1. Description and kinematics

- Recover or regenerate validated SemuBot mesh assets.
- Refine URDF/xacro inertial and collision models.
- Add sensor frame definitions for full perception/navigation integration.

## 2. Hardware abstraction and control

- Integrate existing base and motor drivers through `semubot_hardware` safety wrappers.
- Replace mock odometry integration with validated encoder/IMU-based odometry.
- Expand ros2_control configuration from placeholders to validated controllers.
- Add watchdog and command timeout mechanisms for real hardware safety.

## 3. Perception and interaction

- Replace mock nodes with integrated audio, speech, and vision pipelines.
- Standardize topic contracts and QoS choices for robust runtime behavior.
- Add performance monitoring for real-time interaction components.

## 4. Navigation and manipulation

- Validate full Nav2 prerequisites: TF consistency, odometry quality, and obstacle sensing.
- Add map/localization stack with reproducible configuration and lab validation logs.
- Build MoveIt 2 configuration for arm/head planning groups.
- Connect trajectory execution to verified ros2_control hardware interfaces.

## 5. Testing and evidence automation

- Add CI checks for build, lint, and launch smoke tests.
- Add reproducible integration tests in `semubot_test_tools`.
- Standardize thesis evidence capture workflow (logs, graphs, screenshots, videos).

## 6. Documentation and handover

- Keep README concise and practical.
- Maintain historical context in `docs/previous_work.md`.
- Maintain curated visual evidence in `docs/demos.md` and `media/`.
- Maintain `docs/navigation_readiness.md` as the handover reference for base/Nav2 progress.


## 7. Transition from mock Nav2 to real robot Nav2

- Validate real localization and odometry drift over representative trajectories.
- Replace mock `/scan` with validated lidar or depth-based obstacle sensing.
- Tune footprint, inflation, and controller limits on hardware.
- Stage mock Nav2 integration into supervised real-robot trials with strict safety gating.
