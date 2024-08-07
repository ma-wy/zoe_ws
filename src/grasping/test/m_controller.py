#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
# test to run franka_human_friendly_controller and MoveGroupCommander at the same time

# step 1
# roslaunch franka_human_friendly_controllers cartesian_variable_impedance_controller.launch robot_ip:=192.168.1.110 load_gripper:=True arm_id:=panda
# step 2
# rosrun move_franka test_h_m_controller.py
# step 3
# rosrun rosrun controller_manager controller_manager list


rospy.init_node("m_controller")
# init
m = MoveGroupCommander("panda_arm") #ee_link = panda_link8
ee_link_m = m.get_end_effector_link()

# control orientation via h
dr = 0.3
dz = 0.05
pose = m.get_current_pose() # panda_link8
p_m, q_m = ee_pose_link8_to_ee(pose)
q_orig = q_m
q_rot = angle_axis_to_q([0,0,dr])
q_new = transformation_Q(q_orig,q_rot)
p_m[2] = p_m[2] + dz
pose_target = give_Pose(p_m,q_new)
m.set_pose_target(pose_target, end_effector_link=ee_link_m)

# move
m.go(pose_target, wait=True)





































    
    
    

