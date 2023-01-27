The project's goal is to connect the Webots simulator to the [ROS2-BDI framework](https://github.com/devis12/ROS2-BDI).
The proposed scenario consists of a robot in a world containing obstacles and objects to pick up and place somewhere else.

#Build & Run#
1. To begin with, follow the guide of the ROS2-BDI framework to make sure everything is installed properly.
2. Clone the repository and launch the command ``colcon build --packages-select bdi_spazza spazza spazza_interfaces`` to build the packages.
3. Source with ``source ~/.bashrc``.
3. Launch the Webots package with ros2 launch spazza launcher.launch.py``.
4. Launch the ROS2-BDI framework with ``ros2 launch bdi_spazza offline_launcher.launch.py``.
