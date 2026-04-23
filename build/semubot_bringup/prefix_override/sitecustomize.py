import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mykyta-nesterenko/Nesterenko-thesis-2026-ROS-stack/install/semubot_bringup'
