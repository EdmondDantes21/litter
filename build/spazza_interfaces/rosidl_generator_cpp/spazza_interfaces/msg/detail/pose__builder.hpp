// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from spazza_interfaces:msg/Pose.idl
// generated code does not contain a copyright notice

#ifndef SPAZZA_INTERFACES__MSG__DETAIL__POSE__BUILDER_HPP_
#define SPAZZA_INTERFACES__MSG__DETAIL__POSE__BUILDER_HPP_

#include "spazza_interfaces/msg/detail/pose__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace spazza_interfaces
{

namespace msg
{

namespace builder
{

class Init_Pose_y
{
public:
  explicit Init_Pose_y(::spazza_interfaces::msg::Pose & msg)
  : msg_(msg)
  {}
  ::spazza_interfaces::msg::Pose y(::spazza_interfaces::msg::Pose::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::spazza_interfaces::msg::Pose msg_;
};

class Init_Pose_x
{
public:
  Init_Pose_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Pose_y x(::spazza_interfaces::msg::Pose::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Pose_y(msg_);
  }

private:
  ::spazza_interfaces::msg::Pose msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::spazza_interfaces::msg::Pose>()
{
  return spazza_interfaces::msg::builder::Init_Pose_x();
}

}  // namespace spazza_interfaces

#endif  // SPAZZA_INTERFACES__MSG__DETAIL__POSE__BUILDER_HPP_
