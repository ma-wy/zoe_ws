#!/usr/bin/env python3.8
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__':
    rospy.init_node("rospy_rate_pub")
    rate = rospy.Rate(100) # ROS Rate at 50Hz
    pub = rospy.Publisher("/counter", Int32, queue_size=10)
    counter = 0

    while not rospy.is_shutdown():
        counter += 1
        msg = Int32()
        msg.data = counter
        pub.publish(counter)
        rate.sleep()


    
    
