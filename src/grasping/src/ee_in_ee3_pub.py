#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("ee_in_ee3_pub", anonymous=True)
frame_ch = "panda_EE"
frame_p = "new_EE_3"
listener = tf.TransformListener() 
listener.waitForTransform(frame_p, frame_ch, rospy.Time(), rospy.Duration(40.0))
ee_to_ee3_pub = rospy.Publisher("/ee_in_ee3_tf", Pose, queue_size=1)

while not rospy.is_shutdown():
  (trans, q_rot) = listener.lookupTransform(frame_p, frame_ch, rospy.Time(0))
  pose = give_Pose(trans,q_rot)
  ee_to_ee3_pub.publish(pose)
