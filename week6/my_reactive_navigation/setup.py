from setuptools import find_packages, setup

package_name = 'my_reactive_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='My',
    maintainer_email='my@example.com',
    description='LiDAR reactive navigation package',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'lidar_navigator = my_reactive_navigation.lidar_navigator:main',
    ],
},
)
