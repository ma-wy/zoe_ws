# Calibration of the point cloud on the table plane  
## Procegure  
__Step 1:__ put the chessboard on the table  
__Step 2:__ grasp the calibration tool using franka  
`$ rosrun franka_basic_motion gripper_width.py 0.032`  
__Step 3:__ align the calibration tool with four aruco markers at corners, advise the positions of corners A, B, C (LD, RD, RU) in corner_points.txt  
`$ rosrun franka_basic_motion get_rob_feedback.py` 
__Step 4:__ reset robot  
`$ rosrun franka_basic_motion grasping_init.py grasping`  
__Step 5:__ get folyfit result  
`$ rosrun calibration_table_pc get_polyfit_result.py`  
__Step 6:__ 