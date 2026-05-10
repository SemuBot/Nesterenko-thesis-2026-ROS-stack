# semubot_description

Robot description package for SemuBot.

## Model strategy

- Visual geometry uses actual SemuBot meshes from prior SemuBot description assets.
- Collision geometry is simplified (primitive shapes) for navigation/simulation stability.
- URDF defines robot-local frames only (`base_footprint`, `base_link`, body/sensor frames).
- `odom -> base_link` and `map -> odom` are dynamic transforms and are not fixed in URDF.

## Mesh layout

- `meshes/visual/` detailed visualization meshes
- `meshes/collision/` optional simplified collision meshes (primitives currently used in xacro)
