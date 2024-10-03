#!/usr/bin/env python3.8
import sys
import rospy
from llm_grasping.srv import *
import time


if __name__ == '__main__':
  print('start')
  print(time.time())
  rospy.wait_for_service('llm_rob_fun_server')
  get_rob_signal = rospy.ServiceProxy('llm_rob_fun_server', SetRobFun)
  resp = get_rob_signal('handover')
  print(time.time())
  print(resp.success)
  resp = get_rob_signal('idle')
  print(time.time())
  print(resp.success)
  resp = get_rob_signal('xx')
  print(time.time())
  print(resp.success)
  
    