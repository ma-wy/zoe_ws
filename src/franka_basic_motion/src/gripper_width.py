#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *



width = float(get_argv(value=0.032, index=1))
print(width)


rospy.init_node("gripper_width", anonymous=True)
gripper = MoveGroupCommander('panda_hand')
#print(gripper.get_joints()) #['panda_hand_joint', 'panda_finger_joint1', 'panda_finger_joint2']
#print(gripper.get_named_targets()) #['open', 'close']
#print(gripper.get_named_target_values('open')) # {'panda_finger_joint1': 0.035, 'panda_finger_joint2': 0.035}
#print(gripper.get_named_target_values('close')) # {'panda_finger_joint1': 0.0, 'panda_finger_joint2': 0.0}

print('before moving the gripper')
print(gripper.get_current_joint_values())
gripper.go([width/2, width/2])
print('after moving the gripper')
print(gripper.get_current_joint_values())


    
    
    
    
