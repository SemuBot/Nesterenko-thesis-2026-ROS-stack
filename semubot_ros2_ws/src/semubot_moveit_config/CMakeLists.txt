cmake_minimum_required(VERSION 3.8)
project(semubot_moveit_config)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY docs
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
