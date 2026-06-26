from setuptools import find_packages, setup

package_name = 'my_camera_follower'

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
    description='Camera-based object following package',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'my_camera_follower = my_camera_follower.my_camera_follower:main',
        'clr_follower = my_camera_follower.clr_follower:main',
        'tracking = my_camera_follower.tracking:main',
    ],
},
     )
