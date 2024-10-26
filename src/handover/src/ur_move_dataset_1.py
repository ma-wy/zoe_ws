#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import urx 
import numpy
rob = urx.Robot("169.254.162.54")
rob.set_tcp((0, 0, 0, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
a = 0.2
v = 0.3 
print('before movement')
print(rob.getj())
degree = -10
joints = [0,0,0,0,0,float(degree)/180.0*numpy.pi]
rob.movej(joints, acc=a, vel=v, wait=True, relative=True, threshold=None)
print('after movement')
print(rob.getj())
rob.close()
