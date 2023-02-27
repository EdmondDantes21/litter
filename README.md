# Project description #

The project's goal is to connect the Webots simulator to the [ROS2-BDI framework](https://github.com/devis12/ROS2-BDI).
The proposed scenario consists of a robot in a world containing obstacles and objects to pick up and place somewhere else.

# Build & Run # 

1. To begin with, follow the guide from the [ROS2-BDI framework](https://github.com/devis12/ROS2-BDI) to make sure every necessary component is installed properly.
2. Clone the repository and launch the command ``colcon build`` to build the packages.
3. Source with ``source ~/.bashrc`` if your ``.bashrc`` already contains this project's path, ``source ~/litter/install/local_setup.bash`` to do it manually.

Three different scenario are available, six if we differentiate between online and offline planner. For each scenario two launchers have to be executed (from different terminals), one for ROS2-BDI and the other for Webots.

1. Offline and basic sim: ``ros2 launch bdi_spazza offline_launcher.launch.py`` and ``ros2 launch spazza launcher.launch.py``.
2. Online and basic sim: ``ros2 launch online_bdi_spazza online_launcher.launch.py`` and ``ros2 launch spazza launcher.launch.py``
3. Offline and timer: ``ros2 launch bdi_spazza offline_launcher_time.launch.py`` and ``ros2 launch spawn_spazza launcher_time.launch.py``
4. Online and timer: ``ros2 launch online_bdi_spazza online_launcher_time.launch.py`` and ``ros2 launch spawn_spazza launcher_time.launch.py``
5. Offline and unlimited space: ``ros2 launch bdi_spazza offline_launcher_time.launch.py`` and ``ros2 launch moving_spazza launcher.launch.py``
6. Online and unlimited space: ``ros2 launch moving_bdi_spazza online_launcher_time_bag.launch.py`` and ``ros2 launch moving_spazza launcher.launch.py``
