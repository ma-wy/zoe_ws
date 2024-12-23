// Generated by gencpp from file llm_grasping/RadianToAngleResponse.msg
// DO NOT EDIT!


#ifndef LLM_GRASPING_MESSAGE_RADIANTOANGLERESPONSE_H
#define LLM_GRASPING_MESSAGE_RADIANTOANGLERESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace llm_grasping
{
template <class ContainerAllocator>
struct RadianToAngleResponse_
{
  typedef RadianToAngleResponse_<ContainerAllocator> Type;

  RadianToAngleResponse_()
    : angle(0.0)
    , success(false)  {
    }
  RadianToAngleResponse_(const ContainerAllocator& _alloc)
    : angle(0.0)
    , success(false)  {
  (void)_alloc;
    }



   typedef double _angle_type;
  _angle_type angle;

   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RadianToAngleResponse_

typedef ::llm_grasping::RadianToAngleResponse_<std::allocator<void> > RadianToAngleResponse;

typedef boost::shared_ptr< ::llm_grasping::RadianToAngleResponse > RadianToAngleResponsePtr;
typedef boost::shared_ptr< ::llm_grasping::RadianToAngleResponse const> RadianToAngleResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator2> & rhs)
{
  return lhs.angle == rhs.angle &&
    lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace llm_grasping

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e8773bcd58191e43d4baf3dbd02e77e4";
  }

  static const char* value(const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe8773bcd58191e43ULL;
  static const uint64_t static_value2 = 0xd4baf3dbd02e77e4ULL;
};

template<class ContainerAllocator>
struct DataType< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "llm_grasping/RadianToAngleResponse";
  }

  static const char* value(const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 angle\n"
"bool success\n"
"\n"
;
  }

  static const char* value(const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.angle);
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RadianToAngleResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::llm_grasping::RadianToAngleResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::llm_grasping::RadianToAngleResponse_<ContainerAllocator>& v)
  {
    s << indent << "angle: ";
    Printer<double>::stream(s, indent + "  ", v.angle);
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LLM_GRASPING_MESSAGE_RADIANTOANGLERESPONSE_H
