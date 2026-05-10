# SemuBot Control Architecture (Initial)

This package stores controller configuration for two tracks:

1. **Mock-first development** (`mock_controllers.yaml`) for safe software integration.
2. **Future real robot control** (`controllers.yaml`) for ros2_control-based rollout.

## Safety and rollout notes

- Real motion remains disabled by default in `semubot_hardware`.
- Controller placeholders are intentionally non-operational until wheel and arm hardware interfaces are validated.
- Before enabling physical hardware, confirm command clamping and estop procedures in lab protocol docs.
