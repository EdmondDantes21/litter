// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from spazza_interfaces:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef SPAZZA_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_
#define SPAZZA_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_

#include "spazza_interfaces/msg/detail/position__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<spazza_interfaces::msg::Position>()
{
  return "spazza_interfaces::msg::Position";
}

template<>
inline const char * name<spazza_interfaces::msg::Position>()
{
  return "spazza_interfaces/msg/Position";
}

template<>
struct has_fixed_size<spazza_interfaces::msg::Position>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<spazza_interfaces::msg::Position>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<spazza_interfaces::msg::Position>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // SPAZZA_INTERFACES__MSG__DETAIL__POSITION__TRAITS_HPP_
