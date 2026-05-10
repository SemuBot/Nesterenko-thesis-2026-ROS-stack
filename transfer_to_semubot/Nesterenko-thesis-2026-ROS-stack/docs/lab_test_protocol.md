# Lab Test Protocol (Safety)

This protocol applies to any test that may result in physical SemuBot movement.

## 1. Pre-test setup

1. Place the robot on a stand or inside a clear floor test area.
2. Ensure immediate access to emergency stop or main power disconnect.
3. Verify low velocity limits in launch parameters and hardware safety nodes.
4. Confirm that the operator and observers understand stop procedures.

## 2. Required supervision

- At least one trained person must remain near the robot during tests.
- Autonomous movement must stay disabled unless explicitly required and approved.
- Do not leave the robot unattended while command topics are active.

## 3. Command execution policy

1. Send commands one by one.
2. Observe full response before sending the next command.
3. Use low-speed `/cmd_vel` values during initial verification.
4. Keep `enable_real_motion=false` unless an explicit supervised real test is approved.
5. Immediately stop testing if behavior deviates from expectations.

## 4. Recommended safe command envelope (initial)

- Linear speed <= 0.10 m/s
- Angular speed <= 0.30 rad/s
- `enable_real_motion=false` by default in development and integration sessions

## 5. Navigation readiness safety notes

- Mock odometry and TF publishing (`odom -> base_link`) do not drive real hardware.
- Any future real odometry path must include watchdogs and stop behavior validation.
- Do not connect Nav2 command output to real motor drivers before obstacle sensing is validated.

## 6. Abort conditions

Stop the test immediately if any of these occur:

- Unexpected direction or speed,
- Loss of control communication,
- Sensor/diagnostic anomalies,
- Mechanical noise, vibration, or overheating signs.

## 7. Post-test checklist

- Publish zero velocity command if needed.
- Power down actuators safely.
- Save terminal logs and observation notes.
- Record anomalies as issues/TODOs before next trial.
