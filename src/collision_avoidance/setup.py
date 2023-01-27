from setuptools import setup

package_name = 'collision_avoidance'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/my_world.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_robot.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_robot2.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

#this sets up the package and adds in the data_files variable the newly added files: my_world.wbt, my_robot.udf and robot_launch.py

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = collision_avoidance.collision_avoidance_driver:main',
        ],
    },
)
