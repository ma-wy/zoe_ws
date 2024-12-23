#!/usr/bin/env python3.8
import sys 
#sys.path.append("/home/abml/zoe_ws/lib")
#from mwy_path import *
from geometry_msgs.msg import *
from numpy import *
import rospy
from std_msgs.msg import *
import time
from llm_grasping.srv import SetRobFun, SetRobFunRequest, SetRobFunResponse


class rob_move:
  def __init__(self):
#=======input==================================================================================
    self.service = rospy.Service('/llm_rob_fun_server', SetRobFun, self.callback_response_rob_fun)
    self.target_sub = rospy.Subscriber("/rob_target_pose", Pose, self.callback_rob_target_pose)
#=======output==================================================================================
    #self.if_move_stop_pub = rospy.Publisher("/if_move_stop", Bool, queue_size=10)
#=================================================================================
# members
    rob_fun = ['shelve', 'handover', 'idle']
    self.rob_ref_p = zeros(3)
    self.rob_ref_q = zeros(4)
    self.rob_fun = 'idle'
    #self.rob = urx.Robot("169.254.162.54")
    self.a = 0.01
    self.v = 0.01
    self.r = 0.01
    self.pose_init = []#zeros(7) # tbc
    self.pose_spare_p = zeros(3)
    self.pose_spare_q = zeros(4)#self.pose_init[3:7]
    self.dh = array([0,0,0.1]) # 10cm
    self.dx = array([-0.1,0,0]) # 10cm
    self.table_h = -0.2
    print('server is ready')
    
#===============================================================================================
  def callback_response_rob_fun(self,request):
    rob_ref_p = array(self.rob_ref_p)
    rob_ref_q = array(self.rob_ref_q)
    print(time.time())
    res = SetRobFunResponse()
    res.success = False
    self.rob_fun = request.action
    print("rob_fun = " + str(self.rob_fun))
    
    if self.rob_fun == 'handover':
      print(self.rob_fun)
      pose1 = []#generate_ur_cmd(rob_ref_p + self.dh, rob_ref_q)# hover
      pose2 = []#generate_ur_cmd(rob_ref_p, rob_ref_q)# approach downward
      pose_list = [pose1, pose2]
      #self.rob.movels(pose_list, acc=self.a, vel=self.v, radius=self.r, wait=True, threshold=None)
      #################
      # gripper close #
      #################
      #time.sleep(3)
      pose3 = pose1# pick up to hover
      pose4 = []#generate_ur_cmd(rob_ref_p + self.dx, rob_ref_q)# hand over
      pose_list = [pose3, pose4]
      #self.rob.movels(pose_list, acc=self.a, vel=self.v, radius=self.r, wait=True, threshold=None)
      ################
      # gripper open #
      ################
      #time.sleep(3)
      #self.rob.movel(self.pose_init, acc=self.a, vel=self.v, wait=True, relative=False, threshold=None)
      # return signal
      res.success = True
    elif self.rob_fun == 'shelve':
      print(self.rob_fun)
      pose1 = []#generate_ur_cmd(rob_ref_p + self.dh, rob_ref_q)# hover
      pose2 = []#generate_ur_cmd(rob_ref_p, rob_ref_q)# approach downward
      pose_list = [pose1, pose2]
      #self.rob.movels(pose_list, acc=self.a, vel=self.v, radius=self.r, wait=True, threshold=None)
      #################
      # gripper close #
      #################
      #time.sleep(3)
      pose3 = pose1# pick up
      pose4 = []#generate_ur_cmd(self.pose_spare_p + self.dh, self.pose_spare_q)# hover to a spare place
      pose5 = []#generate_ur_cmd(self.pose_spare_p, self.pose_spare_q)# place
      pose_list = [pose3, pose4, pose5]
      #self.rob.movels(pose_list, acc=self.a, vel=self.v, radius=self.r, wait=True, threshold=None)
      ################
      # gripper open #
      ################
      #time.sleep(3)
      pose_list = [pose4, self.pose_init] # leave and reset
      #self.rob.movels(pose_list, acc=self.a, vel=self.v, radius=self.r, wait=True, threshold=None)
      res.success = True
    else:
      print(self.rob_fun)
      print('please select a function: 1. handover; 2. shelve.')
      self.rob_fun = 'idle'
      res.success = False
    return res
    
  def callback_rob_target_pose(self, data):
    pose = data.data#get_Pose(data)
    
    #grasp_p = array([pose[0], pose[1], self.table_h])
    #handle_p = array([pose[3], pose[4], self.table_h]) 
    
    # comput grasping pose
    #self.rob_ref_p = pose[0:3]
    #self.rob_ref_q = pose[3:7]

def main(args):
  rospy.init_node('rob_move_2', anonymous=True)
  rate = rospy.Rate(20)
  rm = rob_move()

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
  main(sys.argv)
    
    
    
