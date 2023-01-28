# Install script for directory: /home/redi/litter/src/online_bdi_spazza

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/redi/litter/install/online_bdi_spazza")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/" TYPE DIRECTORY FILES "/home/redi/litter/src/online_bdi_spazza/include/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/opt/ros/foxy/lib/python3.8/site-packages/ament_package/template/environment_hook/library_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/library_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza" TYPE EXECUTABLE FILES "/home/redi/litter/build/online_bdi_spazza/move")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move"
         OLD_RPATH "/home/redi/ws2/install/javaff_interfaces/lib:/home/redi/ws2/install/plansys2_executor/lib:/home/redi/ws2/install/lifecycle_msgs/lib:/home/redi/ws2/install/rosgraph_msgs/lib:/home/redi/ws2/install/statistics_msgs/lib:/home/redi/ws2/install/builtin_interfaces/lib:/home/redi/ws2/install/action_msgs/lib:/home/redi/ws2/install/unique_identifier_msgs/lib:/home/redi/ws2/install/std_msgs/lib:/home/redi/ws2/install/rcl_interfaces/lib:/opt/ros/foxy/lib:/home/redi/ws2/install/plansys2_planner/lib:/home/redi/ws2/install/plansys2_problem_expert/lib:/home/redi/ws2/install/plansys2_domain_expert/lib:/home/redi/ws2/install/plansys2_popf_plan_solver/lib:/opt/ros/foxy/lib/x86_64-linux-gnu:/home/redi/ws2/install/plansys2_pddl_parser/lib:/home/redi/ws2/install/plansys2_msgs/lib:/home/redi/ws2/install/plansys2_core/lib:/home/redi/ws2/install/ros2_bdi_core/lib:/home/redi/ws2/install/ros2_bdi_utils/lib:/home/redi/ws2/install/ros2_bdi_skills/lib:/home/redi/ws2/install/ros2_bdi_interfaces/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/move")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza" TYPE EXECUTABLE FILES "/home/redi/litter/build/online_bdi_spazza/pickup")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup"
         OLD_RPATH "/home/redi/ws2/install/javaff_interfaces/lib:/home/redi/ws2/install/plansys2_executor/lib:/home/redi/ws2/install/lifecycle_msgs/lib:/home/redi/ws2/install/rosgraph_msgs/lib:/home/redi/ws2/install/statistics_msgs/lib:/home/redi/ws2/install/builtin_interfaces/lib:/home/redi/ws2/install/action_msgs/lib:/home/redi/ws2/install/unique_identifier_msgs/lib:/home/redi/ws2/install/std_msgs/lib:/home/redi/ws2/install/rcl_interfaces/lib:/opt/ros/foxy/lib:/home/redi/ws2/install/plansys2_planner/lib:/home/redi/ws2/install/plansys2_problem_expert/lib:/home/redi/ws2/install/plansys2_domain_expert/lib:/home/redi/ws2/install/plansys2_popf_plan_solver/lib:/opt/ros/foxy/lib/x86_64-linux-gnu:/home/redi/ws2/install/plansys2_pddl_parser/lib:/home/redi/ws2/install/plansys2_msgs/lib:/home/redi/ws2/install/plansys2_core/lib:/home/redi/ws2/install/ros2_bdi_core/lib:/home/redi/ws2/install/ros2_bdi_utils/lib:/home/redi/ws2/install/ros2_bdi_skills/lib:/home/redi/ws2/install/ros2_bdi_interfaces/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/pickup")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza" TYPE EXECUTABLE FILES "/home/redi/litter/build/online_bdi_spazza/putdown")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown"
         OLD_RPATH "/home/redi/ws2/install/javaff_interfaces/lib:/home/redi/ws2/install/plansys2_executor/lib:/home/redi/ws2/install/lifecycle_msgs/lib:/home/redi/ws2/install/rosgraph_msgs/lib:/home/redi/ws2/install/statistics_msgs/lib:/home/redi/ws2/install/builtin_interfaces/lib:/home/redi/ws2/install/action_msgs/lib:/home/redi/ws2/install/unique_identifier_msgs/lib:/home/redi/ws2/install/std_msgs/lib:/home/redi/ws2/install/rcl_interfaces/lib:/opt/ros/foxy/lib:/home/redi/ws2/install/plansys2_planner/lib:/home/redi/ws2/install/plansys2_problem_expert/lib:/home/redi/ws2/install/plansys2_domain_expert/lib:/home/redi/ws2/install/plansys2_popf_plan_solver/lib:/opt/ros/foxy/lib/x86_64-linux-gnu:/home/redi/ws2/install/plansys2_pddl_parser/lib:/home/redi/ws2/install/plansys2_msgs/lib:/home/redi/ws2/install/plansys2_core/lib:/home/redi/ws2/install/ros2_bdi_core/lib:/home/redi/ws2/install/ros2_bdi_utils/lib:/home/redi/ws2/install/ros2_bdi_skills/lib:/home/redi/ws2/install/ros2_bdi_interfaces/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/online_bdi_spazza/putdown")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE DIRECTORY FILES
    "/home/redi/litter/src/online_bdi_spazza/launch"
    "/home/redi/litter/src/online_bdi_spazza/pddl"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/online_bdi_spazza")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/online_bdi_spazza")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/opt/ros/foxy/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/opt/ros/foxy/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/environment" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/local_setup.bash")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/local_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_environment_hooks/package.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_index/share/ament_index/resource_index/packages/online_bdi_spazza")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/cmake" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_export_include_directories/ament_cmake_export_include_directories-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/cmake" TYPE FILE FILES "/home/redi/litter/build/online_bdi_spazza/ament_cmake_export_libraries/ament_cmake_export_libraries-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza/cmake" TYPE FILE FILES
    "/home/redi/litter/build/online_bdi_spazza/ament_cmake_core/online_bdi_spazzaConfig.cmake"
    "/home/redi/litter/build/online_bdi_spazza/ament_cmake_core/online_bdi_spazzaConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/online_bdi_spazza" TYPE FILE FILES "/home/redi/litter/src/online_bdi_spazza/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/redi/litter/build/online_bdi_spazza/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
