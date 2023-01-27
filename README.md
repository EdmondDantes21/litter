# Project description #

The project's goal is to connect the Webots simulator to the [ROS2-BDI framework](https://github.com/devis12/ROS2-BDI).
The proposed scenario consists of a robot in a world containing obstacles and objects to pick up and place somewhere else.

# Build & Run # 

1. To begin with, follow the guide from the [ROS2-BDI framework](https://github.com/devis12/ROS2-BDI) to make sure every necessary component is installed properly.
2. Clone the repository and launch the command ``colcon build --packages-select bdi_spazza spazza spazza_interfaces`` to build the packages.
3. Source with ``source ~/.bashrc`` if your ``.bashrc`` already contains this project's path, ``source ~/litter/install/local_setup.bash`` to do it manually.
3. Launch the Webots package with ``ros2 launch spazza launcher.launch.py``.
4. Finally,launch the ROS2-BDI framework with the offline version with ``ros2 launch bdi_spazza offline_launcher.launch.py``. If you want to launch the online version instead ``ros2 launch bdi_spazza online_launcher.launch.py``.
