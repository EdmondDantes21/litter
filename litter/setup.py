from setuptools import setup

package_name = 'litter'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/litter_launcher.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/worlds/litter.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/supervisor.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='redi',
    maintainer_email='redi.vreto@studenti.unitn.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_driver = litter.robot_driver:main'
        ],
    },
)
