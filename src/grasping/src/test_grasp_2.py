#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose
from panda import Panda

rospy.init_node("test_grasp_2", anonymous=True)
rob = MoveGroupCommander('panda_arm')
rob.set_end_effector_link("panda_hand")
pose = rob.get_current_pose()
target = pose.pose
target.position.x = 0.5099142496021676
target.position.y = 0.02734649539007098
rob.go(target)

target.position.z = target.position.z + 0.40
rob.go(target)



    
    
    
    

