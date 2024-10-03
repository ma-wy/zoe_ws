// Generated by gencpp from file llm_grasping/SetRobFunResponse.msg
// DO NOT EDIT!


#ifndef LLM_GRASPING_MESSAGE_SETROBFUNRESPONSE_H
#define LLM_GRASPING_MESSAGE_SETROBFUNRESPONSE_H


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
struct SetRobFunResponse_
{
  typedef SetRobFunResponse_<ContainerAllocator> Type;

  SetRobFunResponse_()
    : success(false)  {
    }
  SetRobFunResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetRobFunResponse_

typedef ::llm_grasping::SetRobFunResponse_<std::allocator<void> > SetRobFunResponse;

typedef boost::shared_ptr< ::llm_grasping::SetRobFunResponse > SetRobFunResponsePtr;
typedef boost::shared_ptr< ::llm_grasping::SetRobFunResponse const> SetRobFunResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::llm_grasping::SetRobFunResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::llm_grasping::SetRobFunResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::SetRobFunResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::llm_grasping::SetRobFunResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::SetRobFunResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace llm_grasping

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::llm_grasping::SetRobFunResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "llm_grasping/SetRobFunResponse";
  }

  static const char* value(const ::llm_grasping::SetRobFunResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::llm_grasping::SetRobFunResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetRobFunResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::llm_grasping::SetRobFunResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::llm_grasping::SetRobFunResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LLM_GRASPING_MESSAGE_SETROBFUNRESPONSE_H