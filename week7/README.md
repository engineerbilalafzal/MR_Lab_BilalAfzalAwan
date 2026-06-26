# Week 7: Autonomous Waypoint Navigation with Nav2

## Aim

This lab uses the Nav2 stack to send a TurtleBot3 robot through a sequence of waypoints. The package `my_autonomous_navigation` contains a Python action client that sends `NavigateToPose` goals one by one.

## Package

```text
my_autonomous_navigation
```

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_autonomous_navigation
source install/setup.bash
```

## Run Gazebo

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Run Nav2 with Map

Use the map generated in Week 5:

```bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_navigation2 navigation2.launch.py \
  use_sim_time:=true \
  map:="/home/bilal41/mr labs/MR_Lab/src/week5/maps/my_map.yaml"
```

In RViz, set the initial pose with **2D Pose Estimate** before sending goals.

## Run Waypoint Mission

```bash
ros2 run my_autonomous_navigation waypoint_navigator
```

Custom waypoints can also be passed from the command line:

```bash
ros2 run my_autonomous_navigation waypoint_navigator 1.20 -1.27 0.99 2.77 -1.18 0.99 3.74 -0.47 0.80
```

Each waypoint is provided as:

```text
x y orientation_w
```

## What the Node Does

- Waits for the `navigate_to_pose` action server.
- Sends one waypoint at a time.
- Waits for the result.
- Pauses briefly at each reached waypoint.
- Continues until the mission is complete.

## Useful Checks

```bash
ros2 action list
ros2 topic list | grep costmap
rqt_graph
```

## Observations

- The robot needs a correct initial pose before navigation.
- Costmaps update as the robot moves near obstacles.
- If the robot is blocked, Nav2 may attempt recovery behavior such as replanning, spinning, or backing up.

## Result

The robot was able to receive navigation goals from a custom ROS 2 node and use Nav2 to move between waypoints.
