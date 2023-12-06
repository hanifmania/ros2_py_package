import os
from glob import glob


from setuptools import setup

package_name = 'my_py_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "launch"), glob("launch/*.launch.py")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jannah',
    maintainer_email='mhaniffarhat@gmail.com',
    description='For learning python ROS2 package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_py_node = my_py_package.my_py_node:main',
            'talker = my_py_package.publisher_member_function:main',
            'listener = my_py_package.subscriber_member_function:main',
            'default = my_py_package.default_py_node:main',
            'joy = my_py_package.joy_controller:main',
        ],
    },
)
