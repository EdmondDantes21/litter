cmake_minimum_required(VERSION 3.5)
project(online_bdi_spazza)

# Default to C++17
set(CMAKE_CXX_STANDARD 17)

# find dependencies
find_package(ament_cmake REQUIRED) 
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(spazza_interfaces REQUIRED)
find_package(plansys2_executor REQUIRED)
find_package(ros2_bdi_core REQUIRED)
find_package(ros2_bdi_interfaces REQUIRED)
find_package(ros2_bdi_utils REQUIRED)
find_package(ros2_bdi_skills REQUIRED)
find_package(javaff_interfaces REQUIRED)

include_directories(include)

set(bdi_act_client_dep
  rclcpp
  plansys2_executor
  ros2_bdi_core
  ros2_bdi_interfaces
  ros2_bdi_utils
  ros2_bdi_skills
  javaff_interfaces
)

set(bdi_sensor_dep
  rclcpp
  ros2_bdi_interfaces
  ros2_bdi_utils
  ros2_bdi_skills
)

# #add_library(${PROJECT_NAME} SHARED ${CORE-LIB-SOURCES})
# ament_target_dependencies(${PROJECT_NAME} 
#   ${bdi_act_client_dep}
#   spazza_interfaces
# )

install(DIRECTORY include/  
  DESTINATION include/
)

ament_export_include_directories(include)
ament_export_libraries(${PROJECT_NAME})
ament_export_dependencies(${dependencies})

add_executable(move src/actions/e_puck/move.cpp)
ament_target_dependencies(move ${bdi_act_client_dep})

add_executable(pickup src/actions/e_puck/pickup.cpp)
ament_target_dependencies(pickup ${bdi_act_client_dep})

add_executable(putdown src/actions/e_puck/putdown.cpp)
ament_target_dependencies(putdown ${bdi_act_client_dep})

install(TARGETS
  move
  pickup
  putdown
  
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  pddl
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
