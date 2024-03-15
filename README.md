## commands  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  


## launch structure  
old (include MoveIt demo):  
`$ roslaunch panda_moveit_config franka_control.launch robot_ip:=192.168.1.110`  
new (2 launch):  
`$ roslaunch zoe_ws franka_control.launch robot_ip:=192.168.1.110`  
  
1 (old) $(find franka\_control)/launch/franka_control.launch  
1 (new, launch: 1 launch, 4 nodes) $(dirname)/franka\_control\_in\_franka_ros.launch  
1-1 (launch: 1 node) $(find franka\_gripper)/launch/franka_gripper.launch (1 node)   
1-1-1 (__node__) name="franka\_gripper" pkg="franka\_gripper" type="franka\_gripper_node"  
1-2 (__node__) name="franka\_control" pkg="franka\_control" type="franka\_control_node"  
1-3 (__node__) name="state\_controller\_spawner" pkg="controller_manager" type="spawner" respawn="false"  
1-4 (__node__) name="robot\_state\_publisher" pkg="robot\_state\_publisher" type="robot\_state_publisher"  
1-5 (__node__) name="joint\_state\_publisher" pkg="joint\_state\_publisher" type="joint\_state_publisher"   

2 (launch: 1 node) $(find panda\_moveit\_config)/launch/ros_controllers.launch  
>arg name="transmission" default="position" passed to 1-2  
2-1 (node) pkg="controller_manager" type="spawner" respawn="false"  (repeat node 1-3)
* try to remove this launch  


## node info  
1. 1-1-1 gripper   
`$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`  
franka\_gripper\_node.cpp: publish the topic /franka_gripper/joint_states  
topics:   
```
/franka_gripper/grasp/cancel
/franka_gripper/grasp/feedback  
/franka_gripper/grasp/goal  
/franka_gripper/grasp/result  
/franka_gripper/grasp/status  

/franka\_gripper/gripper_action/cancel  
/franka\_gripper/gripper_action/feedback  
/franka\_gripper/gripper_action/goal  
/franka\_gripper/gripper_action/result  
/franka\_gripper/gripper_action/status  

/franka_gripper/homing/cancel  
/franka_gripper/homing/feedback  
/franka_gripper/homing/goal  
/franka_gripper/homing/result  
/franka_gripper/homing/status  

/franka_gripper/move/cancel  
/franka_gripper/move/feedback  
/franka_gripper/move/goal  
/franka_gripper/move/result  
/franka_gripper/move/status  

/franka_gripper/stop/cancel  
/franka_gripper/stop/feedback  
/franka_gripper/stop/goal  
/franka_gripper/stop/result  
/franka_gripper/stop/status  

/franka\_gripper/joint_states  
```
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
 
2. 1-2 name="franka\_control" pkg="franka\_control" type="franka\_control_node"   
```
Node [/franka_control]  
Publications:   
 * /franka_control/error_recovery/feedback [franka_msgs/ErrorRecoveryActionFeedback]  
 * /franka_control/error_recovery/result [franka_msgs/ErrorRecoveryActionResult]  
 * /franka_control/error_recovery/status [actionlib_msgs/GoalStatusArray]  
 * /franka_state_controller/F_ext [geometry_msgs/WrenchStamped]  
 * /franka_state_controller/franka_states [franka_msgs/FrankaState]  
 * /franka_state_controller/joint_states [sensor_msgs/JointState]  
 * /franka_state_controller/joint_states_desired [sensor_msgs/JointState]  
 * /tf [tf2_msgs/TFMessage]  
  
 * /rosout [rosgraph_msgs/Log]  


Subscriptions:   
 * /franka_control/error_recovery/cancel [unknown type]  
 * /franka_control/error_recovery/goal [unknown type]  

Services:   
 * /controller_manager/list_controller_types  
 * /controller_manager/list_controllers  
 * /controller_manager/load_controller  
 * /controller_manager/reload_controller_libraries  
 * /controller_manager/switch_controller  
 * /controller_manager/unload_controller  
 * /franka_control/connect  
 * /franka_control/disconnect  
 * /franka_control/get_loggers  
 * /franka_control/set_EE_frame  
 * /franka_control/set_K_frame   
 * /franka_control/set_cartesian_impedance  
 * /franka_control/set_force_torque_collision_behavior  
 * /franka_control/set_full_collision_behavior  
 * /franka_control/set_joint_impedance  
 * /franka_control/set_load  
 * /franka_control/set_logger_level  


contacting node http://abml:38503/ ...  
Pid: 85052  
Connections:  
 * topic: /rosout  
    * to: /rosout  
    * direction: outbound (46445 - 127.0.0.1:52052) [13]  
    * transport: TCPROS  
 * topic: /franka_state_controller/joint_states  
    * to: /joint_state_publisher  
    * direction: outbound (46445 - 127.0.0.1:52090) [12]  
    * transport: TCPROS  
```

3. 1-3 name="state\_controller\_spawner" pkg="controller_manager" type="spawner" respawn="false"  
```  
Node [/state_controller_spawner]  
Publications:   
 * /rosout [rosgraph_msgs/Log]  

Subscriptions: None  

Services:   
 * /state_controller_spawner/get_loggers  
 * /state_controller_spawner/set_logger_level  


contacting node http://abml:41701/ ...  
Pid: 85053  
Connections:  
 * topic: /rosout  
    * to: /rosout  
    * direction: outbound (42849 - 127.0.0.1:37650) [8]  
    * transport: TCPROS  
```

4. 1-4 name="robot\_state\_publisher" pkg="robot\_state\_publisher" type="robot\_state_publisher"  
```
Node [/robot_state_publisher]  
Publications:   
 * /rosout [rosgraph_msgs/Log]  
 * /tf [tf2_msgs/TFMessage]  
 * /tf_static [tf2_msgs/TFMessage]  

Subscriptions:   
 * /joint_states [sensor_msgs/JointState]  

Services:   
 * /robot_state_publisher/get_loggers  
 * /robot_state_publisher/set_logger_level  


contacting node http://abml:37851/ ...  
Pid: 85054  
Connections:  
 * topic: /rosout  
    * to: /rosout  
    * direction: outbound (49481 - 127.0.0.1:36768) [11]  
    * transport: TCPROS  
 * topic: /joint_states  
    * to: /joint_state_publisher (http://abml:42555/)  
    * direction: inbound (33910 - abml:44321) [13]  
    * transport: TCPROS  
```

5. 1-5 name="joint\_state\_publisher" pkg="joint\_state\_publisher" type="joint\_state_publisher"   
```
Node [/joint_state_publisher]  
Publications:  
 ** /joint_states [sensor_msgs/JointState]  
 * /rosout [rosgraph_msgs/Log]  

Subscriptions:  
 * /franka_gripper/joint_states [sensor_msgs/JointState]  
 * /franka_state_controller/joint_states [sensor_msgs/JointState]  

Services:   
 * /joint_state_publisher/get_loggers  
 * /joint_state_publisher/set_logger_level  


contacting node http://abml:42555/ ...  
Pid: 85060  
Connections:  
 * topic: /rosout  
    * to: /rosout  
    * direction: outbound (44321 - 127.0.0.1:33908) [9]  
    * transport: TCPROS  
 * topic: /joint_states  
    * to: /robot_state_publisher  
    * direction: outbound (44321 - 127.0.0.1:33910) [7]  
    * transport: TCPROS  
 * topic: /franka_state_controller/joint_states  
    * to: /franka_control (http://abml:38309/)  
    * direction: inbound  
    * transport: TCPROS  
 * topic: /franka_gripper/joint_states  
    * to: /franka_gripper (http://abml:38657/)  
    * direction: inbound  
    * transport: TCPROS  
```
 
 
## test   
1. `$ roslaunch franka_gripper franka_gripper.launch robot_ip:=192.168.1.110`    
  
2. `$ roslaunch pick-and-place franka_control_in_franka_ros.launch robot_ip:=192.168.1.110`  
This file will kill franka_gripper.launch  
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






