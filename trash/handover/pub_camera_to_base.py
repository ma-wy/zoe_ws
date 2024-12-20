#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("camera_to_base_pub", anonymous=True)
frame_p = "base"
frame_ch = "camera_top_color_optical_frame"
listener = tf.TransformListener() 
listener.waitForTransform(frame_p, frame_ch, rospy.Time(), rospy.Duration(40.0))
camera_to_base_pub = rospy.Publisher("/cam_to_base_tf",Pose,queue_size=1)

while not rospy.is_shutdown():
  (trans, q_rot) = listener.lookupTransform(frame_p, frame_ch, rospy.Time(0))
  pose = give_Pose(trans,q_rot)
  camera_to_base_pub.publish(pose)