from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'semubot_face'

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
    description='semubot_face package for SemuBot ROS 2 stack.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mock_face_node = semubot_face.mock_face_node:main',
        ],
    },
)
