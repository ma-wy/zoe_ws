// Generated by gencpp from file llm_grasping/set_rob_funResponse.msg
// DO NOT EDIT!


#ifndef LLM_GRASPING_MESSAGE_SET_ROB_FUNRESPONSE_H
#define LLM_GRASPING_MESSAGE_SET_ROB_FUNRESPONSE_H


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
struct set_rob_funResponse_
{
  typedef set_rob_funResponse_<ContainerAllocator> Type;

  set_rob_funResponse_()
    : success(false)  {
    }
  set_rob_funResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> const> ConstPtr;

}; // struct set_rob_funResponse_

typedef ::llm_grasping::set_rob_funResponse_<std::allocator<void> > set_rob_funResponse;

typedef boost::shared_ptr< ::llm_grasping::set_rob_funResponse > set_rob_funResponsePtr;
typedef boost::shared_ptr< ::llm_grasping::set_rob_funResponse const> set_rob_funResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::llm_grasping::set_rob_funResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::llm_grasping::set_rob_funResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::set_rob_funResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::llm_grasping::set_rob_funResponse_<ContainerAllocator1> & lhs, const ::llm_grasping::set_rob_funResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace llm_grasping

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::llm_grasping::set_rob_funResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "llm_grasping/set_rob_funResponse";
  }

  static const char* value(const ::llm_grasping::set_rob_funResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::llm_grasping::set_rob_funResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct set_rob_funResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::llm_grasping::set_rob_funResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::llm_grasping::set_rob_funResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LLM_GRASPING_MESSAGE_SET_ROB_FUNRESPONSE_H