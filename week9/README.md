# Week 9: Camera-Based Object Following

## Aim

This lab uses a robot camera to detect colored objects and publish velocity commands based on the object's position in the image. The package `my_camera_follower` contains three nodes with increasing levels of behavior.

## Package

```text
my_camera_follower
```

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_camera_follower
source install/setup.bash
```

## Launch Camera Simulation

Use a TurtleBot3 model with a camera:

```bash
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=waffle
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Check that camera images are available:

```bash
ros2 topic list | grep camera
ros2 topic hz /camera/image_raw
```

Optional viewer:

```bash
PYTHONNOUSERSITE=1 rqt_image_view /camera/image_raw
```

## Nodes

Basic red-object tracker:

```bash
ros2 run my_camera_follower tracking
```

Red object follower:

```bash
ros2 run my_camera_follower my_camera_follower
```

Final multi-color follower:

```bash
ros2 run my_camera_follower clr_follower
```

## Topics

```text
Subscribe: /camera/image_raw  sensor_msgs/msg/Image
Publish:   /cmd_vel           geometry_msgs/msg/Twist
```

## Behavior

- The tracker rotates to center a detected object.
- The follower aligns with the object, approaches it, and stops when it is close.
- The final node checks red, blue, and green objects by HSV masks and follows the highest-priority detected color.

## Observations

- Lighting and object color strongly affect detection quality.
- HSV threshold tuning is important for stable tracking.
- A smaller forward speed gives smoother behavior near the target.
- If no object is detected, the robot rotates to search.

## Result

The package demonstrates camera-based perception and closed-loop motion control using OpenCV, `cv_bridge`, and ROS 2 velocity commands.
