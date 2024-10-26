#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *




rospy.init_node("get_rob_feedback", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link('panda_hand_tcp')
print('ee_pose')
print(rob.get_current_pose())
print('joints')
joints = rob.get_current_joint_values()
print(joints)
print(rad_to_deg(joints))
    
    
    
    
