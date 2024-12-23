#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

rob = urx.Robot("169.254.162.54")
a = 0.2
v = 0.3

print('press enter to grasp pose')
input()
pose_init = [-0.08, -0.44, -0.14, 1.138, -2.948, -0.0265]
grasp1 = [[-0.08, -0.7, pose_init[2], 1.138, -2.948, -0.0265], [-0.08, -0.7, -0.24, 1.138, -2.948, -0.0265]]
grasp2 = [[-0.032, -0.745, pose_init[2], 2.07, -2.394, -0.015], [-0.032, -0.745, -0.237, 2.07, -2.394, -0.015]]
spare = [-0.0211, -0.822, -0.235, 1.27, -2.89, -0.025]
rob.movels(grasp2, acc=a, vel=v)
print('press enter to reset')
input()
rob.movel([0,0,0.1,0,0,0], acc=a, vel=v, wait=True, relative=True, threshold=None)
rob.movel(pose_init, acc=a, vel=v, wait=True, relative=False, threshold=None)
rob.close()


    
