# Week 6: LiDAR-Based Reactive Navigation

## Aim

This lab implements a reactive navigation node for TurtleBot3. The node uses LiDAR data from `/scan`, divides the scan into front, left, and right regions, and publishes velocity commands on `/cmd_vel` to avoid nearby obstacles.

## Package

```text
my_reactive_navigation
```

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_reactive_navigation
source install/setup.bash
```

## Run Simulation

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Run Navigation Node

```bash
ros2 run my_reactive_navigation lidar_navigator
```

## RViz

```bash
ros2 run rviz2 rviz2
```

Recommended RViz settings:

```text
Fixed Frame: odom
Add: LaserScan -> /scan
Add: TF
Add: Odometry -> /odom
```

## Node Logic

The node performs three main operations:

1. Cleans invalid LiDAR values by replacing `inf` and `NaN` readings.
2. Extracts front, left, and right scan regions.
3. Drives forward when the front area is clear and turns toward the clearer side when an obstacle is near.

Important code behavior:

```python
front = np.concatenate([ranges[0:20], ranges[340:360]])
left = ranges[60:120]
right = ranges[240:300]
```

```python
if front_dist < self.front_threshold:
    twist.linear.x = 0.0
    twist.angular.z = self.turn_speed or -self.turn_speed
else:
    twist.linear.x = self.forward_speed
```

## Observations

- The robot moves slowly when the path is clear.
- When an obstacle is detected in front, forward motion stops.
- The robot turns toward the side with more free space.
- Threshold values affect how early or late the robot reacts.

## Result

The package demonstrates basic obstacle avoidance using only LiDAR readings and velocity commands.
