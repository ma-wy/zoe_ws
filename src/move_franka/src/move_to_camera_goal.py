#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *
from pose_transform_functions import  array_quat_2_pose, list_2_quaternion, position_2_array, transform_pose
from panda import Panda

class move_franka(Panda):
    def __init__(self):
      super(move_franka, self).__init__()
#input==============================================================================================      
      self.goal_sub = rospy.Subscriber('/camera_goal', Float64MultiArray, self.callback_camera_goal)
      print("current position")
      print(self.curr_pos)
      print("current orientation")
      print(self.curr_q)
      print("ready")
      self.curr_joint
# current ee pose
# rosrun tf tf_echo /panda_link0 /panda_EE
# or
# rostopic echo /cartesian_pose
# input a target pose of the camera
# don't change the orientation
# check camera pose
# rosrun tf tf_echo /panda_link0 /camera_color_optical_frame
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.50, 0.707, -0.707, 0.0, 0.0]"      
# rostopic pub /camera_goal std_msgs/Float64MultiArray "data: [0.48, 0.0, 0.515, 0.707, -0.707, 0.0, 0.0]" 

    def callback_camera_goal(self, data):
      print("get goal of camera")
      pose_cam = data.data # q = [x, y, z, w]
      pose_ee = cam_2_ee_pose(list(pose_cam)) #wxyz
      print(pose_ee)
      p_ee = pose_ee[0:3]
      q_ee = list_2_quaternion(q_w_trans(pose_ee[3:7]))
      goal = array_quat_2_pose(p_ee, q_ee)
      self.goal_pub.publish(goal)
      time.sleep(1)
      print("pose after control")
      print("current position")
      print(self.curr_pos)
      print("current orientation")
      print(self.curr_q)
      print("position error")
      print(array(self.curr_pos)-array(p_ee)) #[ 0.00277345  0.00173121 -0.01243834]


def main(args):
  rospy.init_node("move_to_camera_goal", anonymous=True)
  mf = move_franka()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)
    
    
    
    
