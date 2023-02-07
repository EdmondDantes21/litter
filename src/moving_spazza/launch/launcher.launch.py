import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher, Ros2SupervisorLauncher
from webots_ros2_driver.utils import controller_url_prefix


def generate_launch_description():
    package_dir = get_package_share_directory('moving_spazza')
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'e_puck.urdf')).read_text()
    robot_description_2 = pathlib.Path(os.path.join(package_dir, 'resource', 'e_puck_2.urdf')).read_text()
    supervisor_description = pathlib.Path(os.path.join(package_dir, 'resource', 'supervisor.urdf')).read_text()
    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'moving_litter.wbt')
    )

    ros2_supervisor = Ros2SupervisorLauncher()

    my_robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'e_puck'},
        parameters=[
            {'robot_description': robot_description},
        ],  

        arguments=[
            '--webots-robot-name', 'e_puck',
            '--webots-node-name', 'e_puck'
        ]
    )

    my_robot_driver_2 = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'e_puck_2'},
        parameters=[
            {'robot_description': robot_description_2},
        ],  

        arguments=[
            '--webots-robot-name', 'e_puck_2',
            '--webots-node-name', 'e_puck_2'
        ]
    )

    supervisor_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'supervisor'},
        parameters=[
            {'robot_description': supervisor_description},
        ],  

        arguments=[
            '--webots-robot-name', 'supervisor',
            '--webots-node-name', 'supervisor'
        ]
    )

    return LaunchDescription([
        webots,
        my_robot_driver,
        my_robot_driver_2,
        supervisor_driver,
        ros2_supervisor,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])