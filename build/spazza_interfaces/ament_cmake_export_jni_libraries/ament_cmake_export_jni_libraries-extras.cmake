# generated from
# ament_cmake_export_jni_libraries/cmake/template/ament_cmake_export_jni_libraries.cmake.in

set(_exported_jni_libraries "spazza_interfaces_msg__pose__jni__rosidl_typesupport_fastrtps_c;spazza_interfaces_msg__position__jni__rosidl_typesupport_fastrtps_c;spazza_interfaces_msg__pose__jni__rosidl_typesupport_introspection_c;spazza_interfaces_msg__position__jni__rosidl_typesupport_introspection_c;spazza_interfaces_msg__pose__jni__rosidl_typesupport_c;spazza_interfaces_msg__position__jni__rosidl_typesupport_c")

# append absolute JNI libraries to spazza_interfaces_JNI_LIBRARIES
# warn about not existing paths
if(NOT _exported_jni_libraries STREQUAL "")
  find_package(ament_cmake_core QUIET REQUIRED)
  foreach(_exported_jni_library ${_exported_jni_libraries})
    if(NOT IS_ABSOLUTE "${_exported_jni_library}")
      set(_jni_lib "NOTFOUND")
      find_library(
        _jni_lib NAMES "${_exported_jni_library}"
        PATHS "${spazza_interfaces_DIR}/../../../lib/jni"
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH
      )

      if(NOT _jni_lib)
        # warn about not existing library and ignore it
        message(FATAL_ERROR "Package 'spazza_interfaces' exports the JNI library '${_exported_jni_library}' which couldn't be found")
      elseif(NOT IS_ABSOLUTE "${_jni_lib}")
        # the found library must be an absolute path
        message(FATAL_ERROR "Package 'spazza_interfaces' found the JNI library '${_exported_jni_library}' at '${_jni_lib}' which is not an absolute path")
      elseif(NOT EXISTS "${_jni_lib}")
        # the found library must exist
        message(FATAL_ERROR "Package 'spazza_interfaces' found the JNI library '${_jni_lib}' which doesn't exist")
      else()
        list(APPEND spazza_interfaces_JNI_LIBRARIES "${_jni_lib}")
      endif()

    else()
      if(NOT EXISTS "${_exported_jni_library}")
        message(WARNING "Package 'spazza_interfaces' exports the JNI library '${_exported_jni_library}' which doesn't exist")
      else()
        list(APPEND spazza_interfaces_JNI_LIBRARIES "${_exported_jni_library}")
      endif()

    endif()
  endforeach()
endif()
