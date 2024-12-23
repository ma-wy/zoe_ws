#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

class save_data:
  def __init__(self):
#=======input==================================================================================
    # trajectory
    self.hand_pc_rob_sub = rospy.Subscriber('/hand_pc_rob', PointCloud2, self.callback_hand_rob) 
    self.hand_mp_sub = rospy.Subscriber('/hand_msg', hand_mp, self.callback_hand_2d)
    self.hand_average_depth_sub = rospy.Subscriber("/hand_average_depth", PointStamped, self.callback_hand_average_depth)
    # once per trajectory
    self.cam_to_base_sub = rospy.Subscriber("/cam_to_base_tf", Pose, self.callback_cam_to_base)
    self.handle_to_base_sub = rospy.Subscriber("/handle_to_base_tf", Pose, self.callback_handle_to_base)
    
# members
    self.handedness = ' '
    self.hand_2d = []
    self.hand_3d = []
    self.palm = zeros(3)
    self.cam_to_base = zeros(7) # p q
    self.handle_to_base = zeros(7)
    
    
    
# functions
  def callback_hand_rob(self,data):
    points = []
    for pt in point_cloud2.read_points(data):
      points = points + [pt[0],pt[1],pt[2]]
    self.hand_3d = points
    
  def callback_hand_2d(self,data):
    handedness = data.handedness.data
    if handedness == 'right':
      self.handedness = 0
    elif handedness == 'left':
      self.handedness = 1
    wrist = [data.wrist.x, data.wrist.y, data.wrist.z]
    thumb_tip = [data.thumb_tip.x, data.thumb_tip.y, data.thumb_tip.z]
    index_tip = [data.index_tip.x, data.index_tip.y, data.index_tip.z]
    middle_tip = [data.middle_tip.x, data.middle_tip.y, data.middle_tip.z]
    ring_tip = [data.ring_tip.x, data.ring_tip.y, data.ring_tip.z]
    pinky_tip = [data.pinky_tip.x, data.pinky_tip.y, data.pinky_tip.z]
    index_mcp = [data.index_mcp.x, data.index_mcp.y, data.index_mcp.z]
    middle_mcp = [data.middle_mcp.x, data.middle_mcp.y, data.middle_mcp.z]
    ring_mcp = [data.ring_mcp.x, data.ring_mcp.y, data.ring_mcp.z]
    pinky_mcp = [data.pinky_mcp.x, data.pinky_mcp.y, data.pinky_mcp.z]
    self.hand_2d = wrist + thumb_tip + index_tip + middle_tip + ring_tip + pinky_tip + index_mcp + middle_mcp + ring_mcp + pinky_mcp    
  
  def callback_hand_average_depth(self,data):
    self.palm = get_PointStamped(data)
    
  def callback_cam_to_base(self,data):
    self.cam_to_base = get_Pose(data)
  
  def callback_handle_to_base(self,data):
    self.handle_to_base = get_Pose(data)

# class end=========================================================================================


def main(args):
  rospy.init_node('save_data_1', anonymous=True)
  sd = save_data()
  member_num = 1
  pose_num = 1 
  path = '/home/abml/zoe_ws/src/handover/data/dataset_1/member_' + str(member_num) + '/pose_' + str(pose_num) +'/'
  check_make_clear_folder(path)
  
  
  print("\n============ Press `Enter` save data ============")
  input()
  saveDataStep(sd.cam_to_base, path+'cam_to_base.txt')
  saveDataStep(sd.handle_to_base, path+'handle_to_base.txt')  
  while not rospy.is_shutdown():
    t = time.time()
    print(t)
    saveDataStep([t] + [sd.handedness], path+'handedness.txt')
    saveDataStep([t] + sd.hand_2d, path+'hand_2d.txt')
    saveDataStep([t] + sd.hand_3d, path+'hand_3d.txt')
    saveDataStep([t] + sd.palm, path+'palm.txt')
    rospy.sleep(0.01)

  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
