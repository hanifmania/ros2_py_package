from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare an argument to specify the namespace (optional)
        DeclareLaunchArgument('namespace', default_value='', description='Namespace for nodes'),

        # Start joy_node from the joy package
        Node(
            package='joy', executable='joy_node', output='screen',
            namespace=LaunchConfiguration('namespace'),
            remappings=[
                ('joy', 'custom/joy'),  # Example remapping, change as needed
            ]
        ),

        # Start your custom node (joy_controller.py)
        Node(
            package='my_py_package', executable='joy_controller', output='screen',
            namespace=LaunchConfiguration('namespace'),
        ),

        # A conditionally executed action to log a message (optional)
        LogInfo(
            condition=IfCondition(LaunchConfiguration('namespace') == ''),
            msg="No namespace specified."
        )
    ])



