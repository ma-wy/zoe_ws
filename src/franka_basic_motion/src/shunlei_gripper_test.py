#!/usr/bin/env python3.8
import sys 
sys.path.append("/home/abml/zoe_ws/lib")
from mwy_lib import *

def control_gripper(action):
    # Initialize the ROS node
    rospy.init_node('gripper_control', anonymous=True)

    # Initialize the MoveGroupCommander for the gripper
    gripper = MoveGroupCommander('panda_hand')

    # Set the goal joint tolerance
    gripper.set_goal_joint_tolerance(0.002)

    # Define the open and close widths (in meters)
    open_width = 0.025  # Per finger joint (0.05 total width)
    close_width = 0.001  # Nearly fully closed

    # Perform the action based on user input
    if action == 'open':
        rospy.loginfo("Opening the gripper...")
        gripper.go([open_width, open_width], wait=True)
    elif action == 'close':
        rospy.loginfo("Closing the gripper...")
        gripper.go([close_width, close_width], wait=True)
    else:
        rospy.logwarn("Invalid action. Please specify 'open' or 'close'.")
        return

    # Reset the start state
    gripper.set_start_state_to_current_state()
    rospy.loginfo("Gripper control action completed.")

if __name__ == '__main__':
    try:
        # Get user input for action (open/close)
        action = input("Enter 'open' to open the gripper or 'close' to close the gripper: ").strip().lower()
        control_gripper(action)
    except rospy.ROSInterruptException:
        pass

