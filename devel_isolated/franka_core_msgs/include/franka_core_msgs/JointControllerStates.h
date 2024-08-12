// Generated by gencpp from file franka_core_msgs/JointControllerStates.msg
// DO NOT EDIT!


#ifndef FRANKA_CORE_MSGS_MESSAGE_JOINTCONTROLLERSTATES_H
#define FRANKA_CORE_MSGS_MESSAGE_JOINTCONTROLLERSTATES_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <control_msgs/JointControllerState.h>

namespace franka_core_msgs
{
template <class ContainerAllocator>
struct JointControllerStates_
{
  typedef JointControllerStates_<ContainerAllocator> Type;

  JointControllerStates_()
    : header()
    , controller_name()
    , names()
    , joint_controller_states()  {
    }
  JointControllerStates_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , controller_name(_alloc)
    , names(_alloc)
    , joint_controller_states(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _controller_name_type;
  _controller_name_type controller_name;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> _names_type;
  _names_type names;

   typedef std::vector< ::control_msgs::JointControllerState_<ContainerAllocator> , typename std::allocator_traits<ContainerAllocator>::template rebind_alloc< ::control_msgs::JointControllerState_<ContainerAllocator> >> _joint_controller_states_type;
  _joint_controller_states_type joint_controller_states;





  typedef boost::shared_ptr< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> const> ConstPtr;

}; // struct JointControllerStates_

typedef ::franka_core_msgs::JointControllerStates_<std::allocator<void> > JointControllerStates;

typedef boost::shared_ptr< ::franka_core_msgs::JointControllerStates > JointControllerStatesPtr;
typedef boost::shared_ptr< ::franka_core_msgs::JointControllerStates const> JointControllerStatesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::franka_core_msgs::JointControllerStates_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::franka_core_msgs::JointControllerStates_<ContainerAllocator1> & lhs, const ::franka_core_msgs::JointControllerStates_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.controller_name == rhs.controller_name &&
    lhs.names == rhs.names &&
    lhs.joint_controller_states == rhs.joint_controller_states;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::franka_core_msgs::JointControllerStates_<ContainerAllocator1> & lhs, const ::franka_core_msgs::JointControllerStates_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace franka_core_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
{
  static const char* value()
  {
    return "edf5e0c6d3f96d827825a101e071c998";
  }

  static const char* value(const ::franka_core_msgs::JointControllerStates_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xedf5e0c6d3f96d82ULL;
  static const uint64_t static_value2 = 0x7825a101e071c998ULL;
};

template<class ContainerAllocator>
struct DataType< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
{
  static const char* value()
  {
    return "franka_core_msgs/JointControllerStates";
  }

  static const char* value(const ::franka_core_msgs::JointControllerStates_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n"
"\n"
"string controller_name\n"
"\n"
"string[]  names        # Joint names order for command\n"
"\n"
"control_msgs/JointControllerState[] joint_controller_states \n"
"\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: control_msgs/JointControllerState\n"
"# This message presents current controller state of one joint.\n"
"\n"
"# Header timestamp should be update time of controller state\n"
"Header header\n"
"\n"
"# The set point, that is, desired state.\n"
"float64 set_point\n"
"\n"
"# Current value of the process (ie: latest sensor measurement on the controlled value).\n"
"float64 process_value\n"
"\n"
"# First time-derivative of the process value.\n"
"float64 process_value_dot\n"
"\n"
"# The error of the controlled value, essentially process_value - set_point (for a regular PID implementation).\n"
"float64 error\n"
"\n"
"# Time between two consecutive updates/execution of the control law.\n"
"float64 time_step\n"
"\n"
"# Current output of the controller.\n"
"float64 command\n"
"\n"
"# Current PID parameters of the controller.\n"
"float64 p\n"
"float64 i\n"
"float64 d\n"
"float64 i_clamp\n"
"bool antiwindup\n"
;
  }

  static const char* value(const ::franka_core_msgs::JointControllerStates_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.controller_name);
      stream.next(m.names);
      stream.next(m.joint_controller_states);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct JointControllerStates_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::franka_core_msgs::JointControllerStates_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::franka_core_msgs::JointControllerStates_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "controller_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.controller_name);
    s << indent << "names[]" << std::endl;
    for (size_t i = 0; i < v.names.size(); ++i)
    {
      s << indent << "  names[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.names[i]);
    }
    s << indent << "joint_controller_states[]" << std::endl;
    for (size_t i = 0; i < v.joint_controller_states.size(); ++i)
    {
      s << indent << "  joint_controller_states[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::control_msgs::JointControllerState_<ContainerAllocator> >::stream(s, indent + "    ", v.joint_controller_states[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // FRANKA_CORE_MSGS_MESSAGE_JOINTCONTROLLERSTATES_H
