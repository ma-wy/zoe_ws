# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;pluginlib;realtime_tools;speed_scaling_interface;std_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lspeed_scaling_state_controller".split(';') if "-lspeed_scaling_state_controller" != "" else []
PROJECT_NAME = "speed_scaling_state_controller"
PROJECT_SPACE_DIR = "/home/abml/zoe_ws/install"
PROJECT_VERSION = "0.1.1"
