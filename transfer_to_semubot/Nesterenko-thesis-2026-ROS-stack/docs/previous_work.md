# Previous SemuBot Work and Integration Context

This repository aggregates outcomes from multiple SemuBot thesis and subsystem efforts.
The goal of the current ROS 2 stack is architectural integration, not replacement of historical work.

## 1. Subsystem contributions (summary)

1. **Face and neck mechanisms**
   - Prior mechanical and expression/display experiments are preserved as references.
   - Current stack provides `semubot_face` placeholders and interface boundaries.

2. **Audio and speech**
   - Previous ASR/TTS/audio pipeline experiments inform topic conventions and wrappers.
   - Current stack uses mock nodes first and plans controlled migration into `semubot_audio` and `semubot_speech`.

3. **Vision**
   - Prior camera/recognition experiments are treated as subsystem references.
   - Current stack defines perception package boundaries in `semubot_vision`.

4. **Arm mechanics and servo control**
   - Previous servo and arm control prototypes remain valuable references.
   - Current stack introduces safe gesture-level APIs in `semubot_arm`, with TODO-gated real drivers.

5. **Initial ROS 2 integration**
   - Existing work on URDF, RViz2, `/cmd_vel`, Raspberry Pi motor control, and simulation experiments informs package decomposition and launch strategy.

## 2. How this repository uses previous work

- Preserves historical code and media without destructive rewriting.
- Reuses architectural ideas and interface patterns where safe.
- Moves toward a maintainable package-oriented ROS 2 workspace under `semubot_ros2_ws/src`.

## 3. Referencing old repositories or artifacts

When linking prior projects:
- add concise references (title, author/year, short purpose),
- avoid pasting large duplicated content,
- prefer links to source repositories, thesis documents, or selected media entries.

## 4. Historical vs current status labeling

In documentation and demos, explicitly label items as:
- **Current ROS 2 stack** (implemented in `semubot_ros2_ws/src`), or
- **Historical subsystem work** (legacy/reference artifact).

This prevents confusion for future students onboarding to the active architecture.
