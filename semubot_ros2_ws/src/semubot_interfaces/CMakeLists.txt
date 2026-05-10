cmake_minimum_required(VERSION 3.8)
project(semubot_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/BehaviorState.msg"
  "msg/FaceExpression.msg"
  "msg/GestureCommand.msg"
  "msg/SystemStatus.msg"
  DEPENDENCIES std_msgs builtin_interfaces
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
