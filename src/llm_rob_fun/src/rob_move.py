#!/usr/bin/env python3.8

import sys
import rospy
from moveit_commander import MoveGroupCommander
from std_msgs.msg import Int32, Float64  # Import required message types
import tf
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_path import *
from mwy_lib import *

# Initialize ROS node
rospy.init_node("robot_control", anonymous=True)

# Set up MoveGroup for the Panda arm and gripper
arm = MoveGroupCommander('panda_arm')
gripper = MoveGroupCommander('panda_hand')

# Configure arm parameters
arm.set_end_effector_link('panda_hand_tcp')
arm.set_max_velocity_scaling_factor(0.1)
arm.set_max_acceleration_scaling_factor(0.1)
arm.set_planning_time(10.0)

# Configure gripper parameters
gripper.set_goal_joint_tolerance(0.002)

# Define poses for different actions  
poses = {
    'initial': {'position': [-0.0276, 0.6374, 0.1645], 'orientation': [-0.6814, -0.7286, -0.0618, 0.0321]},
    'grasp': {'position': [-0.1203, 0.6075, -0.0776], 'orientation': [0.6935, 0.7163, -0.0757, 0.0118]},
    'safe': {'position': [-0.1298, 0.6528, 0.0522], 'orientation': [-0.6987, -0.7138, 0.0456, 0.0176]},
    'handover': {'position': [0.1226, 0.5402, 0.0148], 'orientation': [-0.9615, -0.2735, 0.0261, 0.0074]}
}

# Gripper widths
gripper_widths = {
    'open': 0.025,  # Per finger joint (0.05 total width)
    'close': 0.001  # Nearly fully closed
}

# Publishers for additional gripper actions
magnet_pub = rospy.Publisher('/control_magnet', Int32, queue_size=10)
pump_pub = rospy.Publisher('/control_pump', Float64, queue_size=10)
power_pub = rospy.Publisher('/control_power', Int32, queue_size=10)

# Function to move the arm to a named pose using adjusted pose calculation
def move_to_pose(pose_name):
    if pose_name not in poses:
        rospy.logwarn(f"Pose '{pose_name}' not defined.")
        return False
    
    # Get the target pose
    pose = poses[pose_name]
    target_pose = give_PoseStamped('panda_link0', pose['orientation'], pose['position'])

    # Get the current pose
    current_pose = arm.get_current_pose().pose

    # Calculate the position adjustment
    adjusted_pose = current_pose
    adjusted_pose.position.x += (target_pose.pose.position.x - current_pose.position.x)
    adjusted_pose.position.y += (target_pose.pose.position.y - current_pose.position.y)
    adjusted_pose.position.z += (target_pose.pose.position.z - current_pose.position.z)

    # Calculate the orientation adjustment
    current_orientation = [
        current_pose.orientation.x,
        current_pose.orientation.y,
        current_pose.orientation.z,
        current_pose.orientation.w
    ]

    target_orientation = [
        target_pose.pose.orientation.x,
        target_pose.pose.orientation.y,
        target_pose.pose.orientation.z,
        target_pose.pose.orientation.w
    ]

    # Interpolate between the current and target orientations
    interpolated_orientation = tf.transformations.quaternion_slerp(
        current_orientation, target_orientation, 1.0
    )

    adjusted_pose.orientation.x = interpolated_orientation[0]
    adjusted_pose.orientation.y = interpolated_orientation[1]
    adjusted_pose.orientation.z = interpolated_orientation[2]
    adjusted_pose.orientation.w = interpolated_orientation[3]

    # Debug: Print the adjusted pose
    rospy.loginfo(f"Adjusted Pose: {adjusted_pose}")

    # Set the adjusted pose as the target
    arm.set_pose_target(adjusted_pose)

    # Plan and execute the movement
    success = arm.go(wait=True)
    arm.stop()
    arm.clear_pose_targets()

    if success:
        rospy.loginfo(f"Moved to '{pose_name}' pose.")
    else:
        rospy.logwarn(f"Failed to move to '{pose_name}' pose.")
    return success

# Function to control the gripper
def control_gripper(action):
    if action not in gripper_widths:
        rospy.logwarn(f"Gripper action '{action}' not defined.")
        return False

    width = gripper_widths[action]
    
    if action == 'close':
        # Additional actions when closing the gripper
        rospy.loginfo("Activating magnet, pump, and power for gripper close action.")
        magnet_pub.publish(Int32(1))  # Activate the magnet
        rospy.sleep(0.1)  # Small delay for reliable publishing
        pump_pub.publish(Float64(3.8))  # Set pump pressure
        rospy.sleep(0.1)
        power_pub.publish(Int32(1))  # Enable power
        rospy.sleep(0.1)
    elif action == 'open':
        # Additional actions when opening the gripper
        rospy.loginfo("Deactivating magnet and power for gripper open action.")
        magnet_pub.publish(Int32(0))  # Deactivate the magnet
        rospy.sleep(0.1)
        power_pub.publish(Int32(0))  # Disable power
        rospy.sleep(0.1)

    rospy.loginfo(f"{'Opening' if action == 'open' else 'Closing'} the gripper...")
    success = gripper.go([width, width], wait=True)
    gripper.stop()
    if success:
        rospy.loginfo(f"Gripper '{action}' action completed.")
    else:
        rospy.logwarn(f"Gripper '{action}' action failed.")
    return success

# Main loop
if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            # Get user input
            action = input("Enter action (i: initial, g: grasp, c: close gripper, o: open gripper, s: safe, h: handover, q: quit): ").strip().lower()
            
            if action == 'i':
                move_to_pose('initial')
            elif action == 'g':
                move_to_pose('grasp')
            elif action == 'c':
                control_gripper('close')
            elif action == 'o':
                control_gripper('open')
            elif action == 's':
                move_to_pose('safe')
            elif action == 'h':
                move_to_pose('handover')
            elif action == 'q':
                rospy.loginfo("Exiting robot control.")
                break
            else:
                rospy.logwarn("Invalid input. Please enter a valid command.")
    except rospy.ROSInterruptException:
        pass

