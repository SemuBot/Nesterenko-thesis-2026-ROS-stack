cmake_minimum_required(VERSION 3.8)
project(semubot_control)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config docs
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
