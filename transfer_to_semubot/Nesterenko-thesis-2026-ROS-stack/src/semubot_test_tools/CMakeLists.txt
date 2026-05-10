cmake_minimum_required(VERSION 3.8)
project(semubot_test_tools)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY docs launch scripts
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
