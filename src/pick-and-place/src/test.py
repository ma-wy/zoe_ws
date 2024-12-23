#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *

class franka_control_rocker:
  def __init__(self):
#=======input==================================================================================
#    self.rocker_sub = rospy.Subscriber('/filterPoints_1', Float64MultiArray, self.callback_rocker)
#=======output==================================================================================
#    self.gripper_pub = rospy.Publisher('/value_topic', Int64, queue_size=10)
   
#===============================================================================================
# members
    self.radius = 0.0
    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_max_velocity_scaling_factor(0.5)
    self.rob.set_max_acceleration_scaling_factor(0.5)
    self.rob.set_named_target('ready')
    self.ee_p = []
    self.ee_q = []
    self.d_pose = []
    self.gripper = MoveGroupCommander('panda_hand')
# functions

#  def callback_rocker(self,data):
#    self.d_pose = data.data

# class end=========================================================================================
def main(args):
  rospy.init_node('franka_control_rocker', anonymous=True)
  rospy.wait_for_message('move_group/status', GoalStatusArray)
  fcr = franka_control_rocker()
  if fcr.rob.has_end_effector_link():
    ee_id = fcr.rob.get_end_effector_link()
    ee_pose = fcr.rob.get_current_pose(ee_id)
    fcr.ee_p = [ee_pose.pose.position.x, ee_pose.pose.position.y, ee_pose.pose.position.z]
    fcr.ee_q = [ee_pose.pose.orientation.x, ee_pose.pose.orientation.y, ee_pose.pose.orientation.z, ee_pose.pose.orientation.w]
  else:
    print("no link is set as ee") 
  print('current ee p:')
  print(fcr.ee_p)
  print('current ee q:')
  print(fcr.ee_q)
  ee_p_new = array(fcr.ee_p) #+ array([0,0,0.01])
  ee_q_new = fcr.ee_q
  ee_pose_new = list(ee_p_new) + list(ee_q_new)
  print(ee_pose_new)

  fcr.rob.set_pose_target(ee_pose_new, ee_id) #plan time: 0.06890296936035156 ms

  fcr.rob.go() 
  # no change time: 240.22293090820312 ms
  # execute time: 466.43757820129395 ms
#  joint_goal = [0.338380620839303, 0.5052951123337996, 0.04423710695170519, -2.536839071135732, -0.08056383111038141, 2.9986641362303863, 1.2747214452214537]
#  fcr.rob.go(joint_goal, wait=True)
  
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)

