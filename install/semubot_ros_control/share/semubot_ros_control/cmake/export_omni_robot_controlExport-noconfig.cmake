#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "semubot_ros_control::semubot_hardware_interface" for configuration ""
set_property(TARGET semubot_ros_control::semubot_hardware_interface APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(semubot_ros_control::semubot_hardware_interface PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libsemubot_hardware_interface.so"
  IMPORTED_SONAME_NOCONFIG "libsemubot_hardware_interface.so"
  )

list(APPEND _cmake_import_check_targets semubot_ros_control::semubot_hardware_interface )
list(APPEND _cmake_import_check_files_for_semubot_ros_control::semubot_hardware_interface "${_IMPORT_PREFIX}/lib/libsemubot_hardware_interface.so" )

# Import target "semubot_ros_control::semubot_velocity_controller" for configuration ""
set_property(TARGET semubot_ros_control::semubot_velocity_controller APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(semubot_ros_control::semubot_velocity_controller PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libsemubot_velocity_controller.so"
  IMPORTED_SONAME_NOCONFIG "libsemubot_velocity_controller.so"
  )

list(APPEND _cmake_import_check_targets semubot_ros_control::semubot_velocity_controller )
list(APPEND _cmake_import_check_files_for_semubot_ros_control::semubot_velocity_controller "${_IMPORT_PREFIX}/lib/libsemubot_velocity_controller.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
