from setuptools import setup

package_name = 'spawn_spazza'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/launcher.launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/spawn_litter.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/e_puck.urdf']))
data_files.append(('share/' + package_name + '/resource', ['resource/supervisor.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Redi',
    maintainer_email='redi.vreto@studenti.unitn.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = spawn_spazza.e_puck_controller:main',
        ],
    },
)