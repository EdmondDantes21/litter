// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from spazza_interfaces:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef SPAZZA_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
#define SPAZZA_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_

#include "spazza_interfaces/msg/detail/position__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace spazza_interfaces
{

namespace msg
{

namespace builder
{

class Init_Position_theta
{
public:
  explicit Init_Position_theta(::spazza_interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  ::spazza_interfaces::msg::Position theta(::spazza_interfaces::msg::Position::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::spazza_interfaces::msg::Position msg_;
};

class Init_Position_z
{
public:
  explicit Init_Position_z(::spazza_interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_theta z(::spazza_interfaces::msg::Position::_z_type arg)
  {
    msg_.z = std::move(arg);
    return Init_Position_theta(msg_);
  }

private:
  ::spazza_interfaces::msg::Position msg_;
};

class Init_Position_y
{
public:
  explicit Init_Position_y(::spazza_interfaces::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_z y(::spazza_interfaces::msg::Position::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Position_z(msg_);
  }

private:
  ::spazza_interfaces::msg::Position msg_;
};

class Init_Position_x
{
public:
  Init_Position_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Position_y x(::spazza_interfaces::msg::Position::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Position_y(msg_);
  }

private:
  ::spazza_interfaces::msg::Position msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::spazza_interfaces::msg::Position>()
{
  return spazza_interfaces::msg::builder::Init_Position_x();
}

}  // namespace spazza_interfaces

#endif  // SPAZZA_INTERFACES__MSG__DETAIL__POSITION__BUILDER_HPP_
