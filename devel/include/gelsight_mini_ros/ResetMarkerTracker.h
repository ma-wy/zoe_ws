// Generated by gencpp from file gelsight_mini_ros/ResetMarkerTracker.msg
// DO NOT EDIT!


#ifndef GELSIGHT_MINI_ROS_MESSAGE_RESETMARKERTRACKER_H
#define GELSIGHT_MINI_ROS_MESSAGE_RESETMARKERTRACKER_H

#include <ros/service_traits.h>


#include <gelsight_mini_ros/ResetMarkerTrackerRequest.h>
#include <gelsight_mini_ros/ResetMarkerTrackerResponse.h>


namespace gelsight_mini_ros
{

struct ResetMarkerTracker
{

typedef ResetMarkerTrackerRequest Request;
typedef ResetMarkerTrackerResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ResetMarkerTracker
} // namespace gelsight_mini_ros


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::gelsight_mini_ros::ResetMarkerTracker > {
  static const char* value()
  {
    return "652fe242855f56226caf0d487b3cf6bf";
  }

  static const char* value(const ::gelsight_mini_ros::ResetMarkerTracker&) { return value(); }
};

template<>
struct DataType< ::gelsight_mini_ros::ResetMarkerTracker > {
  static const char* value()
  {
    return "gelsight_mini_ros/ResetMarkerTracker";
  }

  static const char* value(const ::gelsight_mini_ros::ResetMarkerTracker&) { return value(); }
};


// service_traits::MD5Sum< ::gelsight_mini_ros::ResetMarkerTrackerRequest> should match
// service_traits::MD5Sum< ::gelsight_mini_ros::ResetMarkerTracker >
template<>
struct MD5Sum< ::gelsight_mini_ros::ResetMarkerTrackerRequest>
{
  static const char* value()
  {
    return MD5Sum< ::gelsight_mini_ros::ResetMarkerTracker >::value();
  }
  static const char* value(const ::gelsight_mini_ros::ResetMarkerTrackerRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::gelsight_mini_ros::ResetMarkerTrackerRequest> should match
// service_traits::DataType< ::gelsight_mini_ros::ResetMarkerTracker >
template<>
struct DataType< ::gelsight_mini_ros::ResetMarkerTrackerRequest>
{
  static const char* value()
  {
    return DataType< ::gelsight_mini_ros::ResetMarkerTracker >::value();
  }
  static const char* value(const ::gelsight_mini_ros::ResetMarkerTrackerRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::gelsight_mini_ros::ResetMarkerTrackerResponse> should match
// service_traits::MD5Sum< ::gelsight_mini_ros::ResetMarkerTracker >
template<>
struct MD5Sum< ::gelsight_mini_ros::ResetMarkerTrackerResponse>
{
  static const char* value()
  {
    return MD5Sum< ::gelsight_mini_ros::ResetMarkerTracker >::value();
  }
  static const char* value(const ::gelsight_mini_ros::ResetMarkerTrackerResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::gelsight_mini_ros::ResetMarkerTrackerResponse> should match
// service_traits::DataType< ::gelsight_mini_ros::ResetMarkerTracker >
template<>
struct DataType< ::gelsight_mini_ros::ResetMarkerTrackerResponse>
{
  static const char* value()
  {
    return DataType< ::gelsight_mini_ros::ResetMarkerTracker >::value();
  }
  static const char* value(const ::gelsight_mini_ros::ResetMarkerTrackerResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // GELSIGHT_MINI_ROS_MESSAGE_RESETMARKERTRACKER_H