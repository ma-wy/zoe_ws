#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

class move_franka():
    def __init__(self):
#input==============================================================================================      
      self.goal_sub = rospy.Subscriber('/camera_goal', Float64MultiArray, self.callback_camera_goal)
      self.rob = MoveGroupCommander('panda_arm')
      self.rob.set_end_effector_link('panda_hand_tcp')
      self.rob.set_max_velocity_scaling_factor(0.1)
      self.rob.set_max_acceleration_scaling_factor(0.1)
      print(self.rob.get_current_pose())
# current ee pose
# rosrun tf tf_echo /panda_link0 /panda_EE
# input a target pose of the camera
# don't change the orientation
# check camera pose
# rosrun tf tf_echo /panda_link0 /camera_color_optical_frame
# handover
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.515, 0.707, -0.707, 0.0, 0.0]" 
# grasping
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.156, 0.449, 0.540, 1.0, 0.0, 0.0, 0.0]"
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [-0.16, 0.45, 0.51, 1.0, 0, 0, 0]"

    def callback_camera_goal(self, data):
      print("get goal of camera")
      pose_cam = data.data # q = [x, y, z, w]
      pose_ee = cam_2_ee_pose(list(pose_cam)) #xyzw
      print(pose_ee)
      p_ee = pose_ee[0:3]
      q_ee = pose_ee[3:7]
      target = give_PoseStamped('panda_link0', q_ee, p_ee)
      print("target")
      print(target)
      self.rob.go(target)
      print('current ee pose')
      print(self.rob.get_current_pose())



def main(args):
  rospy.init_node("move_to_camera_goal", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    


