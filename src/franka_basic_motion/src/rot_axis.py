#!/usr/bin/env python3.8

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

axis = sys.argv[1]
d = float(sys.argv[2])

rospy.init_node("rot_axis", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
frame = "panda_link0"
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)

pose = rob.get_current_pose()
pose_crr = get_PoseStamped(pose)
p_crr = pose_crr[0:3]
q_crr = pose_crr[3:7]
q_rot = angle_axis_to_q_complex(axis = axis, angle = d, angle_type = "degree")
q_new = transformation_Q(q_crr,q_rot)
target = give_PoseStamped(frame, q_new, p_crr)
rob.go(target)









    
    
    

