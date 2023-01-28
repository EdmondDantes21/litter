# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_online_bdi_spazza_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED online_bdi_spazza_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(online_bdi_spazza_FOUND FALSE)
  elseif(NOT online_bdi_spazza_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(online_bdi_spazza_FOUND FALSE)
  endif()
  return()
endif()
set(_online_bdi_spazza_CONFIG_INCLUDED TRUE)

# output package information
if(NOT online_bdi_spazza_FIND_QUIETLY)
  message(STATUS "Found online_bdi_spazza: 0.0.0 (${online_bdi_spazza_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'online_bdi_spazza' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${online_bdi_spazza_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(online_bdi_spazza_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "ament_cmake_export_include_directories-extras.cmake;ament_cmake_export_libraries-extras.cmake")
foreach(_extra ${_extras})
  include("${online_bdi_spazza_DIR}/${_extra}")
endforeach()
