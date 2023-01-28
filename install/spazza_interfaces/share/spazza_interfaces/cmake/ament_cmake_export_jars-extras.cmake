# generated from
# ament_cmake_export_jars/cmake/template/ament_cmake_export_jars.cmake.in

set(_exported_jars "${spazza_interfaces_DIR}/../../../share/spazza_interfaces/java/spazza_interfaces_messages.jar")

# append absolute jars to spazza_interfaces_JARS
# warn about not existing paths
if(NOT _exported_jars STREQUAL "")
  find_package(ament_cmake_core QUIET REQUIRED)
  foreach(_exported_jar ${_exported_jars})
    if(NOT EXISTS "${_exported_jar}")
      message(WARNING "Package 'spazza_interfaces' exports the jar '${_exported_jar}' which doesn't exist")
    else()
      normalize_path(_exported_jar "${_exported_jar}")
      list(APPEND spazza_interfaces_JARS "${_exported_jar}")
    endif()
  endforeach()
endif()
