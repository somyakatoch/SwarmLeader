from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.conditions import IfCondition  # Import IfCondition for conditional actions

def generate_launch_description():
    return LaunchDescription([
        # Declare launch argument for 'leader' node
        DeclareLaunchArgument('leader', default_value='true', description='Launch leader node'),

        # Logging action to notify about the launch (this will always run)
        LogInfo(msg="Launching leader and follower nodes..."),

        # Leader node (only launches if 'leader' is true)
        Node(
            package='leader_follower_swarm',
            executable='leader_node',
            name='leader_node',
            output='screen',
            condition=IfCondition(LaunchConfiguration('leader')),  # Condition to launch leader
        ),

        # Follower node (always launched)
        Node(
            package='leader_follower_swarm',
            executable='follower_node',
            name='follower_node',
            output='screen',
        ),
    ])