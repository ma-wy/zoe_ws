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
#=======output==================================================================================
#===============================================================================================
# members
#311.867 254.023 
#369.615 552.456 460.460 520.072 336.453 172.203 245.607 204.587
    self.bridge = CvBridge()
    #self.row = 720
    #self.col = 1280
    self.row = 480
    self.col = 640
    self.blank_image = np.zeros((self.row,self.col,3), np.uint8)
    self.file_path = '/home/abml/zoe_ws/src/calibration/calibration_table_pc/result/'
    
    
    A = array([-0.4359152372989427, 0.27408421920589665]) # LD
    B = array([0.13389109710454133, 0.27450518990813494]) # RD
    C = array([0.1286924089000353, 0.6429546929864265]) # RU
        
    x_axis = (B-A)/norm(B-A)
    y_axis = (C-B)/norm(C-B)    
        
    P0 = A + 0.0365 * x_axis + 0.0715 * y_axis# LD
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
        
  def callback_rgb(self, data):
    self.blank_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
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
        cv2.drawChessboardCorners(img, pattern_size, corners2, ret)
        print(corners2)
        for i in range(shape(corners2)[0]):
          self.x_2d_list.append(corners2[i,0,0])
          self.y_2d_list.append(corners2[i,0,1])
        # 3d = f(2d)  
        x_param = polyfit(self.x_2d_list, self.x_3d_list, 2)  
        y_param = polyfit(self.y_2d_list, self.y_3d_list, 2) 
        print(x_param)
        print(y_param)
        saveDataStep(x_param, self.file_path + 'x_param.txt', if_clear = True)
        saveDataStep(y_param, self.file_path + 'y_param.txt', if_clear = True)
        print(get_polyfit_result([30,45]))
        print('**************************')
        
    else:
      print('##########################')
# class end=========================================================================================




def main(args):
 
  
  
  rospy.init_node('detect_table', anonymous=True)
  dt = detect_table()

  while not rospy.is_shutdown():
    cv2.imshow("chessboard_detect", dt.blank_image)    
    if cv2.waitKey(1) == ord('q'):
      break
  cv2.destroyAllWindows()   

  try:
    rospy.spin()    
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':

    main(sys.argv)





