import os
import pathlib
import launch
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher, Ros2SupervisorLauncher
from webots_ros2_driver.utils import controller_url_prefix

#https://docs.ros.org/en/foxy/Tutorials/Advanced/Simulators/Webots.html

def generate_launch_description():
    package_dir = get_package_share_directory('collision_avoidance')
    robot_description = pathlib.Path(os.path.join(package_dir, 'resource', 'my_robot.urdf')).read_text()
    robot_description2 = pathlib.Path(os.path.join(package_dir, 'resource', 'my_robot2.urdf')).read_text()
    #allows to open an instance of webots. Need to sepecify the world to open
    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', 'my_world.wbt')
    )

    #launches a supervisor robot
    ros2_supervisor = Ros2SupervisorLauncher()

    #generate new ROS2 node which will be the one controlling the robot
    my_robot_driver = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'my_robot'},
        parameters=[
            {'robot_description': robot_description},
        ],
        arguments=[
            '--webots-robot-name', 'my_robot'
            '--webots-node-name', 'robot1'
        ]
    )

    my_robot_driver2 = Node(
        package='webots_ros2_driver',
        executable='driver',
        output='screen',
        additional_env={'WEBOTS_CONTROLLER_URL': controller_url_prefix() + 'my_robot2'},
        parameters=[
            {'robot_description': robot_description2},
        ],
        arguments=[
            '--webots-robot-name', 'my_robot2',
            '--webots-node-name', 'robot2'
        ]
    )   

    return LaunchDescription([
        webots,
        my_robot_driver,
        my_robot_driver2,
        ros2_supervisor,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        )
    ])
