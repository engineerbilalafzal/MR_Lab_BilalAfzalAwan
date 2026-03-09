import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bilal41/ros2_ws/src/my_first_pkg/install/my_first_pkg'
