## commands  

## launch structure  
old (include MoveIt demo):  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
new (2 launch):  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  
  
1 (old) $(find franka\_control)/launch/franka_control.launch  
1 (new, launch: 1 launch, 4 nodes) $(dirname)/franka\_control\_in\_franka_ros.launch  
1-1 (launch: 1 node) $(find franka\_gripper)/launch/franka_gripper.launch (1 node)   
1-1-1 (node) pkg="franka\_gripper" type="franka\_gripper_node"  
1-2 (node) pkg="franka\_control" type="franka\_control_node"  
1-3 (node) pkg="controller_manager" type="spawner" respawn="false"  
1-4 (node) pkg="robot\_state\_publisher" type="robot\_state_publisher"  
1-5 (node) pkg="joint\_state\_publisher" type="joint\_state_publisher"   

2 (launch: 1 node) $(find panda\_moveit\_config)/launch/ros_controllers.launch  
>arg name="transmission" default="position" passed to 1-2  
2-1 (node) pkg="controller_manager" type="spawner" respawn="false"  


in "franka_control_in_franka_ros.launch"  
`$ roslaunch zoe_ws franka_control_in_franka_ros.launch robot_ip:=192.168.1.110`  


## test  
1. `$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`    
franka\_gripper\_node.cpp: publish the topic /franka_gripper/joint_states  
run:  
`$ rostopic echo /franka_gripper/joint_states`  
output:  
```
header: 
  seq: 9558
  stamp: 
    secs: 1710421306
    nsecs: 571185133
  frame_id: ''
name: 
  - panda_finger_joint1
  - panda_finger_joint2
position: [-1.8386666852165945e-05, -1.8386666852165945e-05]
velocity: [0.0, 0.0]
effort: [0.0, 0.0]
```
This topic publishes the states of the two fingers of the gripper.  
 
2. `$ rosparam load rosparam load ~/catkin_cl/src/franka_ros/franka_control/config/franka_control_node.yaml subst_value:=true`   

3. `$ rosrun franka_control franka_control_node`  
xxx   


4. `$ rosparam load rosparam load ~/catkin_cl/src/franka_ros/franka_control/config/default_controllers.yaml subst_value:=true`  



----------------------------------------
## notes  
* test communication between franka and pc:  
`$ communication_test 192.168.1.110`  
`$ rosrun libfranka communication_test 192.168.1.110`    
`$ ping 192.168.1.110`  


* commands  
`$ source ./catkin_cl/devel/setup.bash`  
(This command had already been added in the ~/.bashrc)
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
`$ python3 scrubnurseicravideo.py`  


* where is franka_control  
run  
`$ rospack find franka_control`  
output  
>/home/abml/catkin_cl/src/franka_ros/franka_control  
 

* $(dirname) in the launch file returns the absolute path of this launch file.  
For example:  
`<include file="$(dirname)/other.launch" />`  
Will expect to find other.launch in the same directory as the launch file which it appears in.  


* look for a python module:  
Opend a terminal, run   
`$ python3`   
`help("moveit_commander")`  
press 'q' to exit  

output:  
>/opt/ros/noetic/lib/python3/dist-packages/moveit_commander/\_\_init\_\_.py  



* franka lib source code   
moveit_commander.robot.RobotCommander.Link	 
moveit_commander.move_group.MoveGroupCommander	 
moveit_commander.interpreter.MoveGroupCommandInterpreter	
moveit_commander.interpreter.MoveGroupInfoLevel	 
moveit_commander.planning_scene_interface.PlanningSceneInterface	
moveit_commander.robot.RobotCommander	 






