# Navigation Readiness and Mobile Base Integration

## Why this phase exists

Full Nav2 autonomy depends on a stable base interface. Before enabling autonomous navigation on real hardware, SemuBot must provide consistent:

- `/cmd_vel` command handling,
- `/odom` publication,
- TF transforms (`odom -> base_link`),
- robot model frames,
- obstacle sensing inputs for local planning.

This phase implements a safe, mock-first baseline for those prerequisites.

## Why Nav2 requires TF, odometry, `/cmd_vel`, and sensors

Nav2 uses:
- **TF** to understand frame relationships (`map`, `odom`, `base_link`, sensor frames),
- **odometry** to estimate short-term robot motion,
- **`/cmd_vel`** as the velocity control interface,
- **range/depth sensing** to avoid obstacles and update local costmaps.

If any of these inputs are inconsistent, navigation behavior becomes unreliable or unsafe.

## Current SemuBot readiness status

Implemented now (mock mode):
- `mock_base_hardware_node` subscribes to `/cmd_vel`.
- Velocity limits are validated in node parameters.
- Mock planar odometry is integrated and published on `/odom`.
- Dynamic `odom -> base_link` TF is published.
- Robot model remains available via `robot_state_publisher` and `joint_state_publisher`.
- Real hardware motion remains disabled by default.

## What is mocked in this phase

- Mobile base motion is simulated by simple planar integration.
- Odometry is synthetic and not sensor-fused.
- No real wheel encoders, IMU fusion, or slip estimation are used.
- Nav2 launch wiring is provided in a guarded/optional form.

## What must be tested on the real robot later

Before real Nav2 trials:
1. Validate encoder/IMU odometry quality and drift.
2. Validate TF consistency under real motion.
3. Validate safe velocity limits and stop behavior.
4. Validate command timeout/watchdog behavior.
5. Validate obstacle sensing coverage and latency.

## Sensors needed for obstacle avoidance

At least one reliable obstacle sensing source is needed, for example:
- 2D lidar (`/scan`), or
- depth camera pipeline with robust obstacle extraction.

Sensor placement, field of view, and update rate must be validated in lab conditions.

## Why full Nav2 remains future work

Full Nav2 is intentionally deferred until:
- odometry is reliable on real hardware,
- obstacle sensing is validated,
- safety behavior is repeatable,
- and runtime performance is stable under realistic test conditions.

This staged approach reduces risk and supports reproducible thesis experimentation.


## Mesh strategy note

The robot visualization now uses actual SemuBot body/head/arm/base meshes where available.
For safety and performance, collision geometry remains simplified for navigation readiness and Nav2 testing.
