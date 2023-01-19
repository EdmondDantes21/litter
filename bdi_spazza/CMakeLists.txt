cmake_minimum_required(VERSION 3.5)
project(bdi_spazza)

# Default to C++17
set(CMAKE_CXX_STANDARD 17)

# find dependencies
find_package(ament_cmake REQUIRED) 
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)

find_package(plansys2_msgs REQUIRED)
find_package(plansys2_executor REQUIRED)
find_package(plansys2_problem_expert REQUIRED)

find_package(ros2_bdi_utils REQUIRED)
find_package(ros2_bdi_interfaces REQUIRED)
find_package(ros2_bdi_skills REQUIRED)
find_package(ros2_bdi_core REQUIRED)

find_package(javaff_interfaces REQUIRED)

find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)  


set(bdi_act_client_dep
    rclcpp
    rclcpp_action
    plansys2_msgs
    plansys2_executor
)

set(bdi_act_client_dep
  rclcpp
  rclcpp_action
  plansys2_msgs
  plansys2_executor
  ros2_bdi_interfaces
  ros2_bdi_utils
  ros2_bdi_skills
  ros2_bdi_core
  javaff_interfaces
)

set(sensors_dep
  rclcpp
  ros2_bdi_interfaces
  ros2_bdi_utils
  ros2_bdi_skills
  ros2_bdi_core
)

add_executable(move src/actions/move.cpp)
ament_target_dependencies(move ${bdi_act_client_dep})

add_executable(pickup src/actions/move.cpp)
ament_target_dependencies(pickup ${bdi_act_client_dep})

add_executable(putdown src/actions/move.cpp)
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
