#!/usr/bin/env python3.8

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

rospy.init_node("reset_gripper_ori", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
frame = "panda_link0"
rob.set_max_velocity_scaling_factor(0.1)
rob.set_max_acceleration_scaling_factor(0.1)

# align z_axis of gripper to minus z axis of base
pose = rob.get_current_pose()
pose_crr = get_PoseStamped(pose)
p_crr = pose_crr[0:3]
q_crr = pose_crr[3:7]
R = tf.transformations.quaternion_matrix(q_crr)
current_z_vec = array(R[0:3, 2])
target_z_vec = array([0,0,-1]) # minus z axis of base
q_rot = rotation_between_2v(current_z_vec, target_z_vec)
q_new = transformation_Q(q_crr,q_rot)
target = give_PoseStamped(frame, q_new, p_crr)
rob.go(target)

# algin y_axis of gripper to x_axis of base
pose = rob.get_current_pose()
pose_crr = get_PoseStamped(pose)
p_crr = pose_crr[0:3]
q_crr = pose_crr[3:7]
R = tf.transformations.quaternion_matrix(q_crr)
current_y_vec = array(R[0:3, 1])
target_y_vec = array([1,0,0]) # y_axis of gripper = x_axis of base
q_rot = rotation_between_2v(current_y_vec, target_y_vec)
q_new = transformation_Q(q_crr,q_rot)
target = give_PoseStamped(frame, q_new, p_crr)
rob.go(target)



    
    
    

