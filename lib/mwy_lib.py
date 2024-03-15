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
  R = tf.transformations.rotation_matrix(norm(r), r/norm(r))
  q = tf.transformations.quaternion_from_matrix(R) 
  return q
  

  
  
  
  
  
  
  
