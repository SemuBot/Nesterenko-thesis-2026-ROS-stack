cmake_minimum_required(VERSION 3.8)
project(semubot_simulation)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY docs launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
