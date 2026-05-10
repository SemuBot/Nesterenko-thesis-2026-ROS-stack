# SemuBot Demos and Visual Evidence

Use this page to curate media evidence without overloading the main README.

> Keep README focused on build/launch/testing. Place most GIFs/screenshots/videos here.

## Media organization

Store files under:
- `media/current_stack/` for current architecture demos
- `media/historical/` for legacy subsystem demos

## 1. Face / neck

- **[TODO]** Add GIF: face expression update pipeline
- Caption template: "Demonstrates expression command handling from `/face/expression` to display output."

## 2. Audio / speech

- **[TODO]** Add screenshot or GIF: speech pipeline mock/status flow
- Caption template: "Shows speech text, response text, and status topic activity in mock mode."

## 3. Vision

- **[TODO]** Add screenshot: perception topic outputs
- Caption template: "Demonstrates mock or real vision outputs for faces/gaze/emotion topics."

## 4. Arms

- **[TODO]** Add GIF/video: gesture command handling
- Caption template: "Shows gesture command reception and arm status updates via safe interface."

## 5. ROS 2 visualization

- **[TODO]** Add screenshot: RViz robot model + TF tree
- Caption template: "Confirms semubot_description model and TF availability in visualization mode."

## 6. Mock robot demo

- **[TODO]** Add screenshot or short video: mock_robot.launch.py running nodes/topics
- Caption template: "Shows integrated mock robot stack with safe cmd_vel receiver and monitor nodes."

## 7. Real robot lab demo

- **[TODO]** Add supervised lab video (low speed only)
- Caption template: "Validated low-speed supervised motion test with safety constraints enabled."

## Recommended embed style

```md
### Example: RViz model (current stack)
![RViz model](../media/current_stack/rviz_model.png)

*Figure: SemuBot model in RViz launched with `visualization.launch.py`.*
```

For videos, link the file path and include a 1-2 sentence explanation of what the demo proves.
