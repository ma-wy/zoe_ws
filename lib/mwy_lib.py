#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

#import sys 
#sys.path.append("/home/abml/zoe_ws/lib")
#from mwy_lib import *


'''
@author: mwy
'''
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *

def d_time_ms(t1, t2):
  t = (t2-t1)*1000.0
  print('time: %s ms' % t)
  return t

def give_PointStamped(frame, p):
  point = PointStamped()
  point.header.frame_id = frame
  point.header.stamp = rospy.Time.now() 
  point.point.x = p[0]
  point.point.y = p[1]
  point.point.z = p[2]
  return point

def give_PoseStamped(frame, q, p):
  pose = PoseStamped()
  pose.header.frame_id = frame
  pose.header.stamp = rospy.Time.now()
  pose.pose.orientation.x = q[0]
  pose.pose.orientation.y = q[1]
  pose.pose.orientation.z = q[2]
  pose.pose.orientation.w = q[3]
  pose.pose.position.x = p[0]
  pose.pose.position.y = p[1]
  pose.pose.position.z = p[2]
  return pose

def give_Path(frame, poses):
  path = Path()
  path.header.frame_id = frame#"camera1_color_optical_frame"
  path.header.stamp = rospy.Time.now()
  path.poses = poses
  return path
  
def give_Pose(p,q):
  pose = Pose()
  pose.orientation.x = q[0]
  pose.orientation.y = q[1]
  pose.orientation.z = q[2]
  pose.orientation.w = q[3]
  pose.position.x = p[0]
  pose.position.y = p[1]
  pose.position.z = p[2]
  return pose
  
def give_PoseArray(frame, poses):
  pose = PoseArray()
  pose.header.frame_id = frame
  pose.header.stamp = rospy.Time.now()
  pose.poses = poses
  return pose

def get_Pose(posestamped):
  pose = [posestamped.pose.position.x, 
    posestamped.pose.position.y, 
    posestamped.pose.position.z, 
    posestamped.pose.orientation.x,
    posestamped.pose.orientation.y,
    posestamped.pose.orientation.z,
    posestamped.pose.orientation.w]
  return pose
  
def get_PoseArray(posearray):
  pose_list = []
  for pose in posearray.poses:
    pose_list.append([
      pose.position.x, 
      pose.position.y, 
      pose.position.z, 
      pose.orientation.x,
      pose.orientation.y,
      pose.orientation.z,
      pose.orientation.w
      ]) 
  return pose_list
  
def get_control_degree(input_button):
  degree = zeros(6)
  if input_button == 'x':
    degree = [1, 0, 0, 0, 0, 0]
  elif input_button == 'y':
    degree = [0, 1, 0, 0, 0, 0]
  elif input_button == 'z':
    degree = [0, 0, 1, 0, 0, 0]
  elif input_button == 'p':
    degree = [0, 0, 0, 1, 0, 0]
  elif input_button == 'a':
    degree = [0, 0, 0, 0, 1, 0]
  elif input_button == 'r':
    degree = [0, 0, 0, 0, 0, 1]
#  print('input: ' + input_button)
#  print(degree)
  return array(degree)

def get_control_direction(input_button):
  direction = 0
  if input_button == '-':
    direction = -1
  elif input_button == '+':
    direction = 1
#  print('input: ' + input_button)
#  print(direction)
  return direction

def transformation_P(v_old,trans,rot):
  transform = tf.transformations.quaternion_matrix(rot)
  transform[0,3] = trans[0]
  transform[1,3] = trans[1]
  transform[2,3] = trans[2]
  v_old = np.append(v_old,1)
  v_old = v_old.reshape((4,1))
  v_new = np.dot(transform,v_old).T
  return array([v_new[0,0],v_new[0,1],v_new[0,2]])

def transformation_Q(q_orig,q_rot):
  q_new = tf.transformations.quaternion_multiply(q_rot,q_orig)
  return array(q_new)

def rot_Q(q_old, q_new):
  transform_old = tf.transformations.quaternion_matrix(q_old)
  transform_new = tf.transformations.quaternion_matrix(q_new)
#  T = dot(inv(transform_old),transform_new)
  T = dot(transform_new,inv(transform_old))
#  T = dot(inv(transform_new),transform_old)
#  T = dot(transform_old,inv(transform_new))
  q_rot = tf.transformations.quaternion_from_matrix(T) 

#  q_old_inv = tf.transformations.quaternion_inverse(q_old)
#  q_rot = tf.transformations.quaternion_multiply(q_new,q_old_inv)
#  q_rot = tf.transformations.quaternion_multiply(q_old_inv,q_new)
  return q_rot

def q_to_angle_axis(q):
  R = tf.transformations.quaternion_matrix(q)
  angle, direc, point = tf.transformations.rotation_from_matrix(R)
  r = np.dot(angle,direc)
  return r

def angle_axis_to_q(r):
  if norm(r) == 0:
    q = array([0,0,0,1])
  else:
    d = norm(r)
    R = tf.transformations.rotation_matrix(d, r/d)
    q = tf.transformations.quaternion_from_matrix(R) 
  return q
  

  
  
  
  
  
  
  
