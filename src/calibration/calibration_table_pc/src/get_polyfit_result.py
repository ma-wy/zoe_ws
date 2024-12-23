#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *
from mwy_path import *



class detect_table:
  def __init__(self):
#=======input==================================================================================
    self.rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
    self.rgb_sub.registerCallback(self.callback_rgb) 
    self.depth_sub = message_filters.Subscriber('/camera/aligned_depth_to_color/image_raw', Image)#, queue_size=2
    self.depth_sub.registerCallback(self.callback_depth) 
#=======output==================================================================================
    self.point_image_pub = rospy.Publisher("/pc_from_image", PointCloud2,queue_size=1)
    self.point_3d_pub = rospy.Publisher("/pc_from_3d", PointCloud2,queue_size=1)
    self.point_corners_pub = rospy.Publisher("/pc_corners", PointCloud2,queue_size=1)
    self.point_polyfit_pub = rospy.Publisher("/pc_from_polyfit", PointCloud2,queue_size=1)
    self.point_bias_pub = rospy.Publisher("/pc_from_bias", PointCloud2,queue_size=1)
    self.point_manual_pub = rospy.Publisher("/pc_from_manual", PointCloud2,queue_size=1)
    
    self.pose_image_pub = rospy.Publisher("/test_pose_image", PoseStamped, queue_size=1)
    self.pose_3d_pub = rospy.Publisher("/test_pose_3d", PoseStamped, queue_size=1)
    self.pose_polyfit_pub = rospy.Publisher("/test_pose_polyfit", PoseStamped, queue_size=1)
    self.pose_bias_pub = rospy.Publisher("/test_pose_bias", PoseStamped, queue_size=1)
#===============================================================================================
# members
#311.867 254.023 
#369.615 552.456 460.460 520.072 336.453 172.203 245.607 204.587
    self.bridge = CvBridge()
    #self.row = 720
    #self.col = 1280
    self.row = 480
    self.col = 640
    self.depth_image = np.zeros((self.row,self.col,3), np.uint8)
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.Cx = 317.494
    self.Cy = 246.239
    self.fx = 607.652
    self.fy = 607.507
    
    self.markers_num = 0
    self.markers = []
    
    self.bias_x = []
    self.bias_y = []
    self.pt = [0,0]
    
    self.p_image = []
    self.p_3d = []
    self.p_polyfit = []
    self.p_bias = []
    
    self.file_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/'
    self.real_3d = loadtxt(self.file_path + 'real_3d.txt')
    
    A = loadtxt(self.file_path + 'corner_points.txt')[0] # LD
    B = loadtxt(self.file_path + 'corner_points.txt')[1] # RD
    C = loadtxt(self.file_path + 'corner_points.txt')[2] # RU


    
    self.A = A
    self.B = B
    self.C = C
    self.d = -0.06   
    rgb = struct.unpack('I', struct.pack('BBBB', 255, 0, 0, 255))[0]
    self.corners = [list(A) + [self.d, rgb], list(B) + [self.d, rgb], list(C) + [self.d, rgb]]        
    #x_axis = (A-B)/norm(A-B) * 0.567/norm(A-B)
    #y_axis = (B-C)/norm(B-C) * 0.367/norm(B-C) 
    #P0 = C + 0.0435 * x_axis + 0.0785 * y_axis # RU
    x_axis = (B-A)/norm(A-B) * 0.567/norm(A-B)
    y_axis = (C-B)/norm(B-C) * 0.367/norm(B-C) 
    P0 = A + 0.0435 * x_axis + 0.0785 * y_axis # RU
    
    P_3d_list = []
    x_3d_list = []
    y_3d_list = []
    for j in range(17):
      for i in range(8):
        P_3d_list.append(P0 + 0.03*j*x_axis + 0.03*i*y_axis)
        x_3d_list.append(P_3d_list[-1][0])
        y_3d_list.append(P_3d_list[-1][1])
        
    self.P_sd_list = P_3d_list
    self.x_3d_list = x_3d_list
    self.y_3d_list = y_3d_list
    self.x_2d_list = []
    self.y_2d_list = []    
    
    ####################
    self.ix = 0
    self.iy = 0
    self.CHOOSE_COLOR = False
    self.TRACK_PT = False
    self.count = 0
    
    self.rob = MoveGroupCommander('panda_arm')
    self.rob.set_end_effector_link('panda_hand_tcp')
    os.system("rosrun franka_basic_motion grasping_init.py grasping")
    
  def on_mouse(self,event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
      self.ix,self.iy = x,y
      self.CHOOSE_COLOR = True    
  ##############################  
    
  def callback_depth(self, data):
    self.depth_image = self.bridge.imgmsg_to_cv2(data, "passthrough")
    
    if self.CHOOSE_COLOR == True:
      self.count += 1

      self.TRACK_PT = True
      self.CHOOSE_COLOR = False
    if self.count > 0:
      self.blank_image = cv2.circle(self.blank_image, [self.ix,self.iy], 3, (0,0,255), 2) 
      # nearest point to the selected point
      dis = []
      for i in range(self.markers_num):
        dis.append(norm(array(self.markers[i,0])-array([self.ix,self.iy])))
      pt_index = dis.index(min(dis))
      print('selected marker position')
      print(pt_index)
      print([self.ix,self.iy])

      #os.system("rosrun franka_basic_motion reset_gripper_ori.py")   
      pose = self.rob.get_current_pose() 
      # image
      pt = self.p_image[pt_index][0:3]
      pt_image = p_cam_2_base(pt)
      target_image = deepcopy(pose)
      target_image.pose.position.x = pt_image[0]
      target_image.pose.position.y = pt_image[1]
      target_image.pose.position.z = self.d 
      target_image.pose.orientation.x = 0.7072621248177164 
      target_image.pose.orientation.y = 0.7069464583326944
      target_image.pose.orientation.z = -0.0015923064346344115 
      target_image.pose.orientation.w = 0.0021110209394748225
      self.pose_image_pub.publish(target_image)
      # real 3d
      pt_3d = self.p_3d[pt_index][0:3]
      target_3d = deepcopy(pose)
      target_3d.pose.position.x = pt_3d[0]
      target_3d.pose.position.y = pt_3d[1]
      target_3d.pose.position.z = self.d
      target_3d.pose.orientation.x = 0.7072621248177164 
      target_3d.pose.orientation.y = 0.7069464583326944
      target_3d.pose.orientation.z = -0.0015923064346344115 
      target_3d.pose.orientation.w = 0.0021110209394748225
      self.pose_3d_pub.publish(target_3d)
      # polyfit
      pt_polyfit = polyfit_2d_to_3d([self.ix,self.iy])
      target_polyfit = deepcopy(pose)
      target_polyfit.pose.position.x = pt_polyfit[0]
      target_polyfit.pose.position.y = pt_polyfit[1]
      target_polyfit.pose.position.z = self.d
      target_polyfit.pose.orientation.x = 0.7072621248177164 
      target_polyfit.pose.orientation.y = 0.7069464583326944
      target_polyfit.pose.orientation.z = -0.0015923064346344115 
      target_polyfit.pose.orientation.w = 0.0021110209394748225
      self.pose_polyfit_pub.publish(target_polyfit)
      # bias
      pt_bias = bias_2d_to_3d(pt[0:2])
      target_bias = deepcopy(pose)
      target_bias.pose.position.x = pt_bias[0]
      target_bias.pose.position.y = pt_bias[1]
      target_bias.pose.position.z = self.d
      target_bias.pose.orientation.x = 0.7072621248177164 
      target_bias.pose.orientation.y = 0.7069464583326944
      target_bias.pose.orientation.z = -0.0015923064346344115 
      target_bias.pose.orientation.w = 0.0021110209394748225
      self.pose_bias_pub.publish(target_bias)
      
      saveDataStep(get_PoseStamped(target_image), self.file_path + 'result_image.txt', if_clear = True)
      saveDataStep(get_PoseStamped(target_3d), self.file_path + 'result_3d.txt', if_clear = True)
      saveDataStep(get_PoseStamped(target_polyfit), self.file_path + 'result_polyfit.txt', if_clear = True)
      saveDataStep(get_PoseStamped(target_bias), self.file_path + 'result_bias.txt', if_clear = True)
    
    if self.TRACK_PT == True:
      '''
      print('press enter to start test')
      print(get_PoseStamped(target_image))
      input()    
      print('testing image result')
      
      #os.system("rosrun franka_basic_motion grasping_init.py grasping")
      #os.system("rosrun franka_basic_motion reset_gripper_ori.py")      
      #self.rob.go(target_image)
      #os.system("rosrun franka_basic_motion trans_axis.py z -0.455")
      print('press enter to test next result')
      input()
      
      print('testing real 3d result')
      print(get_PoseStamped(target_3d))
      os.system("rosrun franka_basic_motion grasping_init.py grasping")
      os.system("rosrun franka_basic_motion reset_gripper_ori.py")      
      self.rob.go(target_3d)
      os.system("rosrun franka_basic_motion trans_axis.py z -0.455")
      print('press enter to test next result')
      print()
      input()
      
      print('testing polyfit result')
      print(get_PoseStamped(target_polyfit))
      os.system("rosrun franka_basic_motion grasping_init.py grasping")
      os.system("rosrun franka_basic_motion reset_gripper_ori.py")      
      self.rob.go(target_polyfit)
      os.system("rosrun franka_basic_motion trans_axis.py z -0.455")
      print('press enter to test next result')
      input()
      
      print('testing bias result')
      print(get_PoseStamped(target_bias))
      os.system("rosrun franka_basic_motion grasping_init.py grasping")
      os.system("rosrun franka_basic_motion reset_gripper_ori.py")      
      self.rob.go(target_bias)
      os.system("rosrun franka_basic_motion trans_axis.py z -0.455")
      input()
      
      print('reset robot')
      os.system("rosrun franka_basic_motion grasping_init.py grasping")
      '''
      self.TRACK_PT = False      
      
    
    
  def callback_rgb(self, data):
    if self.count > 0:
      self.blank_image = cv2.circle(self.blank_image, [self.ix,self.iy], 3, (0,0,255), 2)   
    t1 = time.time()
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    cv2.setMouseCallback('raw_image', self.on_mouse)
    img = self.blank_image
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    corners_vertical = 8  
    corners_horizontal = 17 
    pattern_size = (corners_vertical, corners_horizontal)
 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCornersSB(gray, pattern_size, cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ACCURACY)
    
    
    self.x_2d_list = []
    self.y_2d_list = []    
    if ret:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        #cv2.drawChessboardCorners(img, pattern_size, corners2, ret)
        #print(corners2)
        
        self.markers = corners2
        self.markers_num = shape(corners2)[0]
        for i in range(self.markers_num):
          self.x_2d_list.append(corners2[i,0,0])
          self.y_2d_list.append(corners2[i,0,1])
        # 3d = f(2d)  
        x_param = polyfit(self.x_2d_list, self.x_3d_list, 3)  
        y_param = polyfit(self.y_2d_list, self.y_3d_list, 2) 
        #x_param,_ = curve_fit(func,self.x_2d_list,self.x_3d_list) 
        #y_param,_ = curve_fit(func,self.y_2d_list,self.y_3d_list) 
        
        saveDataStep(x_param, self.file_path + 'x_param.txt', if_clear = True)
        saveDataStep(y_param, self.file_path + 'y_param.txt', if_clear = True)
        #print('**************************')
        # generate pc
        a = 255
        Cx = self.Cx
        Cy = self.Cy
        fx = self.fx
        fy = self.fy
        scale = 1000.0
        
        p_image = []
        p_3d = []
        p_polyfit = []
        p_bias = []
        p_manual = []
        
        for i in range(self.markers_num):
        #for i in range(len(self.real_3d)):
          y = int(corners2[i][0][1])
          x = int(corners2[i][0][0])
          # image
          d = self.depth_image[y][x]
          r = 255 
          g = i
          b = 0
          rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]
          pt1 = [(x-Cx)*d/fx/scale,(y-Cy)*d/fy/scale,float(d)/scale, rgb]
          # trans to the base frame
          B_P_C = [-0.160, 0.458, 0.498]
          B_Q_C = [1.000, -0.004, -0.000, 0.002]
          tempt = [(x-Cx)*d/fx/scale,(y-Cy)*d/fy/scale,float(d)/scale]
          pt1 = list(transformation_P(tempt,B_P_C,B_Q_C)) + [rgb]
          p_image.append(pt1)
          print()
          print(i)
          print(pt1)
          # real 3d
          r = i
          g = 200
          b = 100
          rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]
          pt2 = [self.x_3d_list[i], self.y_3d_list[i], self.d, rgb]  
          if i > 0:  
            #self.bias_x.append(pt1[0]-pt2[0])
            #self.bias_y.append(pt1[1]-pt2[1])
            self.bias_x.append(pt2[0]-pt1[0])
            self.bias_y.append(pt2[1]-pt1[1])
            
          p_3d.append(pt2)  
                    
          # fit
          r = 100 
          g = 0
          b = 100 
          rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]
          pt3 = [polyfit_2d_to_3d([x,y])[0], polyfit_2d_to_3d([x,y])[1], self.d, rgb]
          p_polyfit.append(pt3)
          
        # pc from image
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'# 'camera_color_optical_frame' # 
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = list(p_image)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_image_pub.publish(outputPoints)
        # pc from 3d
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = list(p_3d)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_3d_pub.publish(outputPoints)   
        
        # pc from 3d
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = list(p_3d)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_3d_pub.publish(outputPoints)  
        # pc from manual
        r = 200
        g = 200
        b = 100
        d = self.d                                        
        rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]  
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = list(list(i) + [self.d, rgb] for i in self.real_3d)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_manual_pub.publish(outputPoints)                 
        
        # pc from polyfit
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = list(p_polyfit)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_polyfit_pub.publish(outputPoints)
        
        # corners    
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        POINTS = self.corners#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_corners_pub.publish(outputPoints)         
        # pc from bias
        r = 150
        g = 200
        b = 0
        d = self.d                                        
        rgb = struct.unpack('I', struct.pack('BBBB', int(b), int(g), int(r), a))[0]  
        #  pt1[0]-pt2[0] = bias_x.mean, pt1[1]+pt2[1] = bias_y.mean()
        saveDataStep([array(self.bias_x).mean(), array(self.bias_y).mean()], self.file_path + 'bias.txt', if_clear = True)
        HEADER = Header()
        HEADER.frame_id = 'panda_link0'
        FIELDS = [
          PointField('x', 0, PointField.FLOAT32, 1),
          PointField('y', 4, PointField.FLOAT32, 1),
          PointField('z', 8, PointField.FLOAT32, 1),
          PointField('rgb', 12, PointField.UINT32, 1),
        ]
        p_bias = list(list(array(i[0:2])*array([1,-1]) + [-array(self.bias_x).mean(), array(self.bias_y).mean()]) + [d, rgb] for i in p_image) 
        POINTS = list(p_bias)#list
        outputPoints = point_cloud2.create_cloud(HEADER, FIELDS, POINTS)
        self.point_bias_pub.publish(outputPoints)
        #print(norm(array(p_3d[0][0:3])-array(self.corners[2][0:3])))      # C 
        #print(norm(array(p_3d[7][0:3])-array(self.corners[1][0:3])))      
        #print(norm(array(p_3d[-1][0:3])-array(self.corners[0][0:3]))) 
        #print(norm(array(self.corners[1][0:3])-array(self.corners[0][0:3])))
        #print(norm(array(self.corners[1][0:3])-array(self.corners[2][0:3])))
        self.p_image = p_image
        self.p_3d = p_3d
        self.p_polyfit = p_polyfit
        self.p_bias = p_bias
        
    else:
      a = 1
      #print('no chessboard detected')
      #print('##########################')
    t2 = time.time()
    #d_time_ms(t1, t2)
    ##########################################################  
      
# class end=========================================================================================




def main(args):
  
  rospy.init_node('detect_table', anonymous=True)
  dt = detect_table()

  while not rospy.is_shutdown():
    cv2.imshow("raw_image", dt.blank_image)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)





