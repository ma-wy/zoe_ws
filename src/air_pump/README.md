## Air Pump  
### command:  
__step 1__  
unplug the Arduino to check which name disappeared  
check the port name:  
`ls /dev/`  
__step 2__  
`rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600`  
`rosrun rosserial_python serial_node.py /dev/port_name`  
output:  
```  
[INFO] [1711443649.197924]: ROS Serial Python Node
[INFO] [1711443649.202890]: Connecting to /dev/ttyACM0 at 57600 baud
[INFO] [1711443651.313960]: Requesting topics...
[INFO] [1711443651.336107]: Note: subscribe buffer size is 512 bytes
[INFO] [1711443651.337412]: Setup subscriber on value_topic [std_msgs/Int64]
^C[INFO] [1711443732.591054]: Sending tx stop request
[INFO] [1711443732.592487]: shutdown hook activated
```  
__step 3__  
subscriber on value_topic [std_msgs/Int64]:  
give a positive air pressure:  
`rostopic pub /value_topic std_msgs/Int64 "data: 1" `  
stop the air stream (0 pressure):  
`rostopic pub /value_topic std_msgs/Int64 "data: -1" `  
__step 4__
`rostopic echo /value_topic`  


`rostopic pub /control_magnet std_msgs/Int32 "data: 1" `  
`rostopic pub /control_magnet std_msgs/Int32 "data: 0" `  
`rostopic pub /control_pump std_msgs/Float64 "data: 3.8" `  



P.S.  
1. in scrubnurseicravideo.py:  
`pub_gripper = rospy.Publisher('/value_topic', Int64, queue_size=10)`   
`pub_gripper.publish(1)`  

2. location of ros package rosserial_python
`rospack find rosserial_python`  
output:  
`/home/abml/catkin_cl/src/rosserial/rosserial_python`  
location of the node serial_node.py  
`/home/abml/catkin_cl/src/rosserial/rosserial_python/nodes/serial_node.py`  

3. location of sketchbook of Arduino  
`/home/abml/Arduino/sketch_apr13a/sketch_apr13a.ino`  
the libs installed via Arduino IDE are at 
`/home/abml/Arduino/libraries`  




