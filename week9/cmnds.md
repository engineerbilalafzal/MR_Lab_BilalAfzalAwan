# Week 9 Commands: Camera-Based Object Following

## Build Workspace

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_camera_follower
source install/setup.bash
```

## Launch Camera-Enabled TurtleBot3

Use `waffle` or `waffle_pi`, because `burger` usually does not publish camera images.

```bash
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Verify Camera Topic

```bash
ros2 topic list | grep camera
ros2 topic hz /camera/image_raw
```

Optional image viewer:

```bash
rqt_image_view /camera/image_raw
```

If RQT has a NumPy/Matplotlib issue:

```bash
PYTHONNOUSERSITE=1 rqt_image_view /camera/image_raw
```

## Run Basic Red Tracker

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_camera_follower tracking
```

## Run Red Object Follower

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_camera_follower my_camera_follower
```

## Run Final Multi-Color Follower

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run my_camera_follower clr_follower
```

## Debug Topics

```bash
ros2 topic echo /cmd_vel
ros2 node list
ros2 node info /object_tracking
```

