#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose
from panda import Panda

rospy.init_node('test_gripper', anonymous=True)
commander = MoveGroupCommander('panda_hand')
commander.set_named_target('open')
commander.go()
    
    
    
