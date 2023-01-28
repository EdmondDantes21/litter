
#include <jni.h>

#include <cassert>
#include <cstdint>
#include <string>

#include "rosidl_runtime_c/message_type_support_struct.h"

#include "rcljava_common/exceptions.hpp"
#include "rcljava_common/signatures.hpp"


#include "spazza_interfaces/msg/position.h"

// Ensure that a jlong is big enough to store raw pointers
static_assert(sizeof(jlong) >= sizeof(std::intptr_t), "jlong must be able to store pointers");

using rcljava_common::exceptions::rcljava_throw_exception;

#ifdef __cplusplus
extern "C" {
#endif

// Initialize cached types in the anonymous namespace to avoid linking conflicts
namespace
{
JavaVM * g_vm = nullptr;

jclass _jspazza_interfaces__msg__Position_class_global = nullptr;
jmethodID _jspazza_interfaces__msg__Position_constructor_global = nullptr;


jclass _jjava__lang__Double_class_global = nullptr;
jmethodID _jjava__lang__Double_constructor_global = nullptr;

jmethodID _jjava__lang__Double_value_global = nullptr;

}  // namespace

/*
 * Class:     spazza_interfaces_msg_Position
 * Method:    getFromJavaConverter
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getFromJavaConverter
  (JNIEnv *, jclass);

/*
 * Class:     spazza_interfaces_msg_Position
 * Method:    getToJavaConverter
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getToJavaConverter
  (JNIEnv *, jclass);

/*
 * Class:     spazza_interfaces_msg_Position
 * Method:    getTypeSupport
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getTypeSupport
  (JNIEnv *, jclass);

/*
 * Class:     spazza_interfaces_msg_Position
 * Method:    getDestructor
 * Signature: ()J
 */
JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getDestructor
  (JNIEnv *, jclass);

#ifdef __cplusplus
}
#endif

spazza_interfaces__msg__Position * spazza_interfaces_msg_Position__convert_from_java(jobject _jmessage_obj, spazza_interfaces__msg__Position * ros_message)
{
  JNIEnv * env = nullptr;
  // TODO(esteve): check return status
  assert(g_vm != nullptr);
  g_vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6);
  assert(env != nullptr);

  if (ros_message == nullptr) {
    ros_message = spazza_interfaces__msg__Position__create();
  }
  auto _jfield_x_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "x", "D");
  ros_message->x = env->GetDoubleField(_jmessage_obj, _jfield_x_fid);

  auto _jfield_y_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "y", "D");
  ros_message->y = env->GetDoubleField(_jmessage_obj, _jfield_y_fid);

  auto _jfield_z_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "z", "D");
  ros_message->z = env->GetDoubleField(_jmessage_obj, _jfield_z_fid);

  auto _jfield_theta_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "theta", "D");
  ros_message->theta = env->GetDoubleField(_jmessage_obj, _jfield_theta_fid);

  assert(ros_message != nullptr);
  return ros_message;
}

jobject spazza_interfaces_msg_Position__convert_to_java(spazza_interfaces__msg__Position * _ros_message, jobject _jmessage_obj)
{
  JNIEnv * env = nullptr;
  // TODO(esteve): check return status
  assert(g_vm != nullptr);
  g_vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6);
  assert(env != nullptr);

  if (_jmessage_obj == nullptr) {
    _jmessage_obj = env->NewObject(_jspazza_interfaces__msg__Position_class_global, _jspazza_interfaces__msg__Position_constructor_global);
  }
  auto _jfield_x_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "x", "D");
  env->SetDoubleField(_jmessage_obj, _jfield_x_fid, _ros_message->x);
  auto _jfield_y_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "y", "D");
  env->SetDoubleField(_jmessage_obj, _jfield_y_fid, _ros_message->y);
  auto _jfield_z_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "z", "D");
  env->SetDoubleField(_jmessage_obj, _jfield_z_fid, _ros_message->z);
  auto _jfield_theta_fid = env->GetFieldID(_jspazza_interfaces__msg__Position_class_global, "theta", "D");
  env->SetDoubleField(_jmessage_obj, _jfield_theta_fid, _ros_message->theta);
  assert(_jmessage_obj != nullptr);
  return _jmessage_obj;
}

JNIEXPORT jint JNICALL JNI_OnLoad(JavaVM * vm, void *)
{
  // Can only call this once
  if (g_vm == nullptr) {
    g_vm = vm;
  }

  JNIEnv * env;
  if (g_vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6) != JNI_OK) {
    return JNI_ERR;
  } else {
    auto _jspazza_interfaces__msg__Position_class_local = env->FindClass("spazza_interfaces/msg/Position");
    assert(_jspazza_interfaces__msg__Position_class_local != nullptr);
    _jspazza_interfaces__msg__Position_class_global = static_cast<jclass>(env->NewGlobalRef(_jspazza_interfaces__msg__Position_class_local));
    env->DeleteLocalRef(_jspazza_interfaces__msg__Position_class_local);
    assert(_jspazza_interfaces__msg__Position_class_global != nullptr);
    _jspazza_interfaces__msg__Position_constructor_global = env->GetMethodID(_jspazza_interfaces__msg__Position_class_global, "<init>", "()V");
    assert(_jspazza_interfaces__msg__Position_constructor_global != nullptr);
    auto _jjava__lang__Double_class_local = env->FindClass("java/lang/Double");
    assert(_jjava__lang__Double_class_local != nullptr);
    _jjava__lang__Double_class_global = static_cast<jclass>(env->NewGlobalRef(_jjava__lang__Double_class_local));
    env->DeleteLocalRef(_jjava__lang__Double_class_local);
    assert(_jjava__lang__Double_class_global != nullptr);
    _jjava__lang__Double_constructor_global = env->GetMethodID(_jjava__lang__Double_class_global, "<init>", "(D)V");
    assert(_jjava__lang__Double_constructor_global != nullptr);
    _jjava__lang__Double_value_global = env->GetMethodID(_jjava__lang__Double_class_global, "doubleValue", "()D");
    assert(_jjava__lang__Double_value_global != nullptr);
  }
  return JNI_VERSION_1_6;
}

JNIEXPORT void JNICALL JNI_OnUnload(JavaVM * vm, void *)
{
  assert(g_vm != nullptr);
  assert(g_vm == vm);

  JNIEnv * env;
  if (g_vm->GetEnv(reinterpret_cast<void **>(&env), JNI_VERSION_1_6) == JNI_OK) {
    if (_jspazza_interfaces__msg__Position_class_global != nullptr) {
      env->DeleteGlobalRef(_jspazza_interfaces__msg__Position_class_global);
      _jspazza_interfaces__msg__Position_class_global = nullptr;
      _jspazza_interfaces__msg__Position_constructor_global = nullptr;
    }
    if (_jjava__lang__Double_class_global != nullptr) {
      env->DeleteGlobalRef(_jjava__lang__Double_class_global);
      _jjava__lang__Double_class_global = nullptr;
      _jjava__lang__Double_constructor_global = nullptr;
      _jjava__lang__Double_value_global = nullptr;
    }
  }
}

JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getFromJavaConverter(JNIEnv *, jclass)
{
  jlong ptr = reinterpret_cast<jlong>(&spazza_interfaces_msg_Position__convert_from_java);
  return ptr;
}

JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getToJavaConverter(JNIEnv *, jclass)
{
  jlong ptr = reinterpret_cast<jlong>(spazza_interfaces_msg_Position__convert_to_java);
  return ptr;
}

JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getTypeSupport(JNIEnv *, jclass)
{
  jlong ptr = reinterpret_cast<jlong>(ROSIDL_GET_MSG_TYPE_SUPPORT(spazza_interfaces,msg,Position));
  return ptr;
}

JNIEXPORT jlong JNICALL Java_spazza_1interfaces_msg_Position_getDestructor(JNIEnv *, jclass)
{
  jlong ptr = reinterpret_cast<jlong>(spazza_interfaces__msg__Position__destroy);
  return ptr;
}
