# Media Guidelines

This folder stores screenshots, GIFs, and videos used as thesis and engineering evidence.

## Folder layout recommendation

- `media/current_stack/` -> demos of the active ROS 2 architecture
- `media/historical/` -> legacy subsystem demos from previous thesis work

## What media files are allowed

- Optimized screenshots (`.png`, `.jpg`)
- Short optimized GIFs (`.gif`)
- Short videos (`.mp4`) when GIF quality/size is insufficient

## Media quality and size recommendations

- Prefer small, optimized assets suitable for Git repositories.
- Crop to focus on relevant evidence (RViz, topic graph, robot behavior).
- Avoid uploading long raw recordings; keep originals externally if needed.

## Documentation policy

- Keep README lightweight (1-3 selected current-stack visuals maximum).
- Place most media references in `docs/demos.md`.
- Clearly label each media item as:
  - **Current ROS 2 stack evidence**, or
  - **Historical subsystem demo**.

## Suggested naming convention

`YYYYMMDD_<subsystem>_<mode>_<short_description>.<ext>`

Examples:
- `20260503_visualization_mock_rviz_model.png`
- `20260503_behavior_mock_demo_state.gif`
- `20260503_lab_base_low_speed_test.mp4`
