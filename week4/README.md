# Week 4: Launch Files, Rosbag, and RQT Plot

## Aim

This lab focused on running multiple ROS 2 nodes using launch files, recording topic data with rosbag, and plotting velocity data. The main package is `my_launch_pkg`.

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_launch_pkg
source install/setup.bash
```

## Launch Two Turtles

```bash
ros2 launch my_launch_pkg two_turtles_launch.py
```

## Run Follower Node

```bash
ros2 run my_launch_pkg follow_leader
```

## Record Data

```bash
ros2 bag record /turtle1/pose /turtle1/cmd_vel /turtle2/pose /turtle2/cmd_vel
```

Stop recording with `Ctrl+C`.

Replay:

```bash
ros2 bag play <bag_folder>
```

## RQT Plot

```bash
PYTHONNOUSERSITE=1 rqt
```

Add these fields in the Plot plugin:

```text
/turtle1/cmd_vel/linear/x
/turtle1/cmd_vel/angular/z
```

## Result

The launch file started the simulator, spawned a second turtle, and opened teleoperation windows. The follower node used pose feedback to publish velocity commands for the second turtle. Rosbag and RQT were used to inspect the behavior after the run.
