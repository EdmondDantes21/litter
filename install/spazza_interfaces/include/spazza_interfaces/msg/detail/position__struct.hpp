// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from spazza_interfaces:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef SPAZZA_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_
#define SPAZZA_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__spazza_interfaces__msg__Position __attribute__((deprecated))
#else
# define DEPRECATED__spazza_interfaces__msg__Position __declspec(deprecated)
#endif

namespace spazza_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Position_
{
  using Type = Position_<ContainerAllocator>;

  explicit Position_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
      this->theta = 0.0;
    }
  }

  explicit Position_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->z = 0.0;
      this->theta = 0.0;
    }
  }

  // field types and members
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _z_type =
    double;
  _z_type z;
  using _theta_type =
    double;
  _theta_type theta;

  // setters for named parameter idiom
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const double & _arg)
  {
    this->z = _arg;
    return *this;
  }
  Type & set__theta(
    const double & _arg)
  {
    this->theta = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    spazza_interfaces::msg::Position_<ContainerAllocator> *;
  using ConstRawPtr =
    const spazza_interfaces::msg::Position_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<spazza_interfaces::msg::Position_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<spazza_interfaces::msg::Position_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      spazza_interfaces::msg::Position_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<spazza_interfaces::msg::Position_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      spazza_interfaces::msg::Position_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<spazza_interfaces::msg::Position_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<spazza_interfaces::msg::Position_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<spazza_interfaces::msg::Position_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__spazza_interfaces__msg__Position
    std::shared_ptr<spazza_interfaces::msg::Position_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__spazza_interfaces__msg__Position
    std::shared_ptr<spazza_interfaces::msg::Position_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Position_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    if (this->theta != other.theta) {
      return false;
    }
    return true;
  }
  bool operator!=(const Position_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Position_

// alias to use template instance with default allocator
using Position =
  spazza_interfaces::msg::Position_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace spazza_interfaces

#endif  // SPAZZA_INTERFACES__MSG__DETAIL__POSITION__STRUCT_HPP_
