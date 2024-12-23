# UR Packages  
__Donnot use ros-industrial version!__  
## ur_modern_driver  
`git clone -b iron-kinetic-devel https://github.com/iron-ox/ur_modern_driver.git`  
### Notes:  
In the file `src/ur_hardware_interface.cpp`, replace `controller_it->hardware_interface` with `controller_it->type`.

## universal_robot  
`git clone -b calibration_devel https://github.com/rxjia/fmauch_universal_robot.git`  
### Notes:  
1. Under the path `path/to/universal_robot-melodic-devel`,  

| right | wrong |  
| --- | --- |   
| <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/1.png align=center /> | <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/3.png align=center /> |  

2. Under the path `path/to/universal_robot-melodic-devel/ur5_moveit_config/config`,   

| right | wrong |    
| --- | --- |   
| <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/2.png align=center /> | <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/4.png align=center /> |  

3. In the file `controllers.yaml`  

| right | wrong |    
| --- | --- |   
| <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/5.png align=center /> | <img src=https://github.com/ma-wy/zoe_ws/blob/main/src/UR/markdown_source/6.png align=center />|  

4. Under the path `path/to/universal_robot-melodic-devel/ur5_moveit_config/launch`, if `moveit_rviz.launch` cannot run correctly, replace the content with ros-industrial verion.

## Useage:  
`$ roslaunch roslaunch ur_modern_driver ur5_bringup.launch robot_ip:=169.254.162.54`  
`$ roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch`  
`$ roslaunch ur5_moveit_config moveit_rviz.launch`  
