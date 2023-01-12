import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher, Ros2SupervisorLauncher
from webots_ros2_driver.utils import controller_url_prefix  

def generate_launch_description():
    package_dir = get_package_share_directory('litter')
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'supervisor.urdf')).read_text()
    #allows to open an instance of webots. Need to sepecify the world to open
    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'litter.wbt')
    )

    #launches a supervisor robot
    #ros2_supervisor = Ros2SupervisorLauncher()

    #generate new ROS2 node which will be the one controlling the robot
    supervisor = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'supervisor'},
        parameters=[
            {'robot_description': robot_description},
        ],
        arguments=[
            '--webots-robot-name', 'supervisor'
            '--webots-node-name', 'supervisor'
        ]
    )

    return LaunchDescription([
        webots,
        supervisor,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
