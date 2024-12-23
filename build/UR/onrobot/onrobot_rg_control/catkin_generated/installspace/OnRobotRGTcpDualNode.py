#!/usr/bin/env python3
import sys
sys.path.append("/home/abml/zoe_ws/src/UR/onrobot/onrobot_rg_control/src/onrobot_rg_control")
sys.path.append("/home/abml/zoe_ws/src/UR/onrobot/onrobot_rg_modbus_tcp/src/onrobot_rg_modbus_tcp")

import rospy
import baseOnRobotRG
import comModbusTcp
from std_srvs.srv import Trigger, TriggerResponse
from onrobot_rg_control.msg import OnRobotRGInput
from onrobot_rg_control.msg import OnRobotRGOutput


class OnRobotDualRGTcp:
    """ OnRobotDualRGTcp connects to the dual grippers with Modbus/TCP.

        Attributes:
            gripper_primary (baseOnRobotRG.onrobotbaseRG):
                instance for the connection establishment with primary RG
            gripper_secondary (onrobotbaseRG):
                instance for the connection establishment with secondary RG
            pub_primary_gripper (rospy.Publisher):
                the publisher OnRobotRGInput_A for OnRobotRGInput
            pub_secondaray_gripper (rospy.Publisher):
                the publisher OnRobotRGInput_B for OnRobotRGInput

            restartPowerCycle:
                Restarts the power cycle of the gripper.
            mainLoop:
                Loops the sending status and command, and receiving message.
    """

    def __init__(self):
        # Dual quicker changer addresses for both sides using ModBus/TCP
        primary_address = 66  # 0x42
        secondary_address = 67  # 0x43

        # Primary side Gripper on Dual Changer Connection
        self.gripper_primary = \
            baseOnRobotRG.onrobotbaseRG(gtype_prime)
        self.gripper_primary.client = \
            comModbusTcp.communication(dummy)
        self.gripper_primary.client.connectToDevice(
            ip, port, primary_address)

        # Secondary side Gripper on Dual changer Connection
        self.gripper_secondary = \
            baseOnRobotRG.onrobotbaseRG(gtype_second)
        self.gripper_secondary.client = \
            comModbusTcp.communication(dummy)
        self.gripper_secondary.client.connectToDevice(
            ip, port, secondary_address)

        # Grippers Status publish
        self.pub_primary_gripper = rospy.Publisher(
            'OnRobotRGInput_A', OnRobotRGInput, queue_size=1)
        self.pub_secondary_gripper = rospy.Publisher(
            'OnRobotRGInput_B', OnRobotRGInput, queue_size=1)

        # Gripper Commandds reception
        rospy.Subscriber('OnRobotRGOutput_A',
                         OnRobotRGOutput,
                         self.gripper_primary.refreshCommand)
        rospy.Subscriber('OnRobotRGOutput_B',
                         OnRobotRGOutput,
                         self.gripper_secondary.refreshCommand)

        # The restarting service
        rospy.Service(
            "/onrobot_rg/restart_power",
            Trigger,
            self.restartPowerCycle)

        self.mainLoop()

    def restartPowerCycle(self, request):
        """ Restarts the power cycle of the gripper. """

        rospy.loginfo("Restart the power cycle of all grippers connected.")
        self.gripper_primary.restartPowerCycle()
        rospy.sleep(1)
        return TriggerResponse(
            success=None,  # TODO: implement
            message=None)  # TODO: implement

    def mainLoop(self):
        """ Loops the sending status and command, and receiving message. """

        prev_msg_prime = []
        prev_msg_second = []
        while not rospy.is_shutdown():
            # Getting grippers status
            status_primary = self.gripper_primary.getStatus()
            status_secondary = self.gripper_secondary.getStatus()
            # Publishing status
            self.pub_primary_gripper.publish(status_primary)
            self.pub_secondary_gripper.publish(status_secondary)

            rospy.sleep(0.05)
            # Updating command of primary side
            if not int(format(status_primary.gSTA, '016b')[-1]):  # not busy
                # Getting new messages
                if not prev_msg_prime == self.gripper_primary.message:
                    rospy.loginfo(
                        rospy.get_name()+": Sending Message A Side")
                    self.gripper_primary.sendCommand()
                prev_msg_prime = self.gripper_primary.message
            # Updating command of secondary side
            if not int(format(status_secondary.gSTA, '016b')[-1]):  # not busy
                # Getting new messages
                if not prev_msg_second == self.gripper_secondary.message:
                    rospy.loginfo(
                        rospy.get_name()+": Sending Message B Side")
                    self.gripper_secondary.sendCommand()
                prev_msg_second = self.gripper_secondary.message
            rospy.sleep(0.05)


if __name__ == '__main__':
    try:
        ip = rospy.get_param('/onrobot/ip', '192.168.1.1')
        port = rospy.get_param('/onrobot/port', '502')
        gtype_prime = rospy.get_param('/onrobot/gripper_primary', 'rg2')
        gtype_second = rospy.get_param('/onrobot/gripper_secondary', 'rg6')
        dummy = rospy.get_param('/onrobot/dummy', False)
        rospy.init_node(
            'OnRobotDualRGTcp', anonymous=True, log_level=rospy.DEBUG)
        OnRobotDualRGTcp()
    except rospy.ROSInterruptException:
        pass
