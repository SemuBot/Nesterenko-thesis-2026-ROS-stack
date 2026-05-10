from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'semubot_hardware'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='semubot',
    maintainer_email='semubot@todo.todo',
    description='semubot_hardware package for SemuBot ROS 2 stack.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'safe_cmd_vel_receiver_node = semubot_hardware.safe_cmd_vel_receiver_node:main',
            'mock_base_hardware_node = semubot_hardware.mock_base_hardware_node:main',
            'mock_scan_node = semubot_hardware.mock_scan_node:main',
            'hardware_status_node = semubot_hardware.hardware_status_node:main',
        ],
    },
)
