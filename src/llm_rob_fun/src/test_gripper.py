#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *


def main(args):
  rospy.init_node('test_gripper', anonymous=True)
  rate = rospy.Rate(20)
  gripper_grasp_client = actionlib.SimpleActionClient('/franka_gripper/grasp', franka_gripper.msg.GraspAction)
  gripper_grasp_client.wait_for_server()  
 
  
  gripper_move_client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)
  gripper_move_client.wait_for_server()  
  
  
  gripper_homing_client = actionlib.SimpleActionClient('/franka_gripper/homing', franka_gripper.msg.HomingAction)
  gripper_homing_client.wait_for_server() 
  print('ready to grasp')
#  time.sleep(3)
  a = franka_close_gripper(client = gripper_grasp_client, speed=0.1)
  print(a)
#  time.sleep(2)
  b = franka_open_gripper(client=gripper_move_client, width=0.2, speed=0.1)
  print(b)
#  print(franka_close_gripper(client = gripper_grasp_client, speed=0.1))
#  print(franka_homing_gripper(client = gripper_homing_client))
  



    
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)

    
    
