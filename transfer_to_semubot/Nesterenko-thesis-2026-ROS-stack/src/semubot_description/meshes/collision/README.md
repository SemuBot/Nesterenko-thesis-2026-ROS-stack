# Collision mesh strategy

This folder is reserved for optional simplified collision meshes.

Current approach:
- Navigation uses simplified primitive collision geometry directly in xacro.
- Detailed visual meshes in `meshes/visual/` are not used as collision geometry.

Future work:
- Add lightweight simplified STL/DAE collision meshes only if needed for specific planners/simulators.
