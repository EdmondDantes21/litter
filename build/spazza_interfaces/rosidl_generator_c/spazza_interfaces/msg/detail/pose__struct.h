// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from spazza_interfaces:msg/Pose.idl
// generated code does not contain a copyright notice

#ifndef SPAZZA_INTERFACES__MSG__DETAIL__POSE__STRUCT_H_
#define SPAZZA_INTERFACES__MSG__DETAIL__POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/Pose in the package spazza_interfaces.
typedef struct spazza_interfaces__msg__Pose
{
  int16_t x;
  int16_t y;
} spazza_interfaces__msg__Pose;

// Struct for a sequence of spazza_interfaces__msg__Pose.
typedef struct spazza_interfaces__msg__Pose__Sequence
{
  spazza_interfaces__msg__Pose * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} spazza_interfaces__msg__Pose__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // SPAZZA_INTERFACES__MSG__DETAIL__POSE__STRUCT_H_
