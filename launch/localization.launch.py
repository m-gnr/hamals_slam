from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('hamals_slam')

    params_file = os.path.join(
        pkg_share,
        'config',
        'localization.yaml'
    )

    return LaunchDescription([

        Node(
            package='slam_toolbox',
            executable='localization_slam_toolbox_node',
            name='slam_toolbox',
            parameters=[params_file],
            output='screen'
        )
    ])