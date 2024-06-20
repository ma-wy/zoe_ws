## *********************************************************
##
## File autogenerated for the franka_ros_controllers package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'position_joint_delta_filter', 'type': 'double', 'default': 0.3, 'level': 0, 'description': 'Filter parameter that dictates how smoothly subsequent joint position commands are smoothed. Also responsible for speed of joint position execution.', 'min': 0.1, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'velocity_joint_delta_filter', 'type': 'double', 'default': 0.3, 'level': 0, 'description': 'Filter parameter that dictates how smoothly subsequent joint velocity commands are smoothed. Also responsible for acceleration of joints.', 'min': 0.1, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [{'name': 'Controller_Gains', 'type': '', 'state': True, 'cstate': 'true', 'id': 1, 'parent': 0, 'parameters': [{'name': 'j1_k', 'type': 'double', 'default': 1200.0, 'level': 0, 'description': 'Stiffness parameter of joint 1', 'min': 200.0, 'max': 1500.0, 'srcline': 20, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j2_k', 'type': 'double', 'default': 1000.0, 'level': 0, 'description': 'Stiffness parameter of joint 2', 'min': 200.0, 'max': 1500.0, 'srcline': 21, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j3_k', 'type': 'double', 'default': 1000.0, 'level': 0, 'description': 'Stiffness parameter of joint 3', 'min': 200.0, 'max': 1500.0, 'srcline': 22, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j4_k', 'type': 'double', 'default': 800.0, 'level': 0, 'description': 'Stiffness parameter of joint 4', 'min': 200.0, 'max': 1500.0, 'srcline': 23, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j5_k', 'type': 'double', 'default': 300.0, 'level': 0, 'description': 'Stiffness parameter of joint 5', 'min': 100.0, 'max': 1000.0, 'srcline': 24, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j6_k', 'type': 'double', 'default': 200.0, 'level': 0, 'description': 'Stiffness parameter of joint 6', 'min': 75.0, 'max': 500.0, 'srcline': 25, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j7_k', 'type': 'double', 'default': 50.0, 'level': 0, 'description': 'Stiffness parameter of joint 7', 'min': 20.0, 'max': 200.0, 'srcline': 26, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j1_d', 'type': 'double', 'default': 50.0, 'level': 0, 'description': 'Damping parameter of joint 1', 'min': 0.0, 'max': 200.0, 'srcline': 28, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j2_d', 'type': 'double', 'default': 50.0, 'level': 0, 'description': 'Damping parameter of joint 2', 'min': 0.0, 'max': 200.0, 'srcline': 29, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j3_d', 'type': 'double', 'default': 50.0, 'level': 0, 'description': 'Damping parameter of joint 3', 'min': 0.0, 'max': 200.0, 'srcline': 30, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j4_d', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Damping parameter of joint 4', 'min': 0.0, 'max': 200.0, 'srcline': 31, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j5_d', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Damping parameter of joint 5', 'min': 0.0, 'max': 200.0, 'srcline': 32, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j6_d', 'type': 'double', 'default': 20.0, 'level': 0, 'description': 'Damping parameter of joint 6', 'min': 0.0, 'max': 200.0, 'srcline': 33, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'j7_d', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Damping parameter of joint 7', 'min': 0.0, 'max': 200.0, 'srcline': 34, 'srcfile': '/home/abml/zoe_ws/src/Franka/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 124, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT::CONTROLLER_GAINS', 'parentclass': 'DEFAULT', 'parentname': 'Default', 'field': 'DEFAULT::controller_gains', 'upper': 'CONTROLLER_GAINS', 'lower': 'controller_gains'}], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']
