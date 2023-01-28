// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from spazza_interfaces:msg/Pose.idl
// generated code does not contain a copyright notice
#include "spazza_interfaces/msg/detail/pose__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
spazza_interfaces__msg__Pose__init(spazza_interfaces__msg__Pose * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  return true;
}

void
spazza_interfaces__msg__Pose__fini(spazza_interfaces__msg__Pose * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
}

bool
spazza_interfaces__msg__Pose__are_equal(const spazza_interfaces__msg__Pose * lhs, const spazza_interfaces__msg__Pose * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  return true;
}

bool
spazza_interfaces__msg__Pose__copy(
  const spazza_interfaces__msg__Pose * input,
  spazza_interfaces__msg__Pose * output)
{
  if (!input || !output) {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  return true;
}

spazza_interfaces__msg__Pose *
spazza_interfaces__msg__Pose__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  spazza_interfaces__msg__Pose * msg = (spazza_interfaces__msg__Pose *)allocator.allocate(sizeof(spazza_interfaces__msg__Pose), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(spazza_interfaces__msg__Pose));
  bool success = spazza_interfaces__msg__Pose__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
spazza_interfaces__msg__Pose__destroy(spazza_interfaces__msg__Pose * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    spazza_interfaces__msg__Pose__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
spazza_interfaces__msg__Pose__Sequence__init(spazza_interfaces__msg__Pose__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  spazza_interfaces__msg__Pose * data = NULL;

  if (size) {
    data = (spazza_interfaces__msg__Pose *)allocator.zero_allocate(size, sizeof(spazza_interfaces__msg__Pose), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = spazza_interfaces__msg__Pose__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        spazza_interfaces__msg__Pose__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
spazza_interfaces__msg__Pose__Sequence__fini(spazza_interfaces__msg__Pose__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      spazza_interfaces__msg__Pose__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

spazza_interfaces__msg__Pose__Sequence *
spazza_interfaces__msg__Pose__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  spazza_interfaces__msg__Pose__Sequence * array = (spazza_interfaces__msg__Pose__Sequence *)allocator.allocate(sizeof(spazza_interfaces__msg__Pose__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = spazza_interfaces__msg__Pose__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
spazza_interfaces__msg__Pose__Sequence__destroy(spazza_interfaces__msg__Pose__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    spazza_interfaces__msg__Pose__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
spazza_interfaces__msg__Pose__Sequence__are_equal(const spazza_interfaces__msg__Pose__Sequence * lhs, const spazza_interfaces__msg__Pose__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!spazza_interfaces__msg__Pose__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
spazza_interfaces__msg__Pose__Sequence__copy(
  const spazza_interfaces__msg__Pose__Sequence * input,
  spazza_interfaces__msg__Pose__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(spazza_interfaces__msg__Pose);
    spazza_interfaces__msg__Pose * data =
      (spazza_interfaces__msg__Pose *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!spazza_interfaces__msg__Pose__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          spazza_interfaces__msg__Pose__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!spazza_interfaces__msg__Pose__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
