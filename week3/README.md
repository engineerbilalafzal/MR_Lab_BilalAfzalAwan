# Week 3: Custom Turtlesim Control Package

## Aim

The goal of this lab was to create a custom ROS 2 Python package and write nodes that control Turtlesim motion. The package `my_turtle_package` contains nodes for moving the turtle in different patterns and moving it toward a target location.

## Package

```text
my_turtle_package
```

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_turtle_package
source install/setup.bash
```

## Run Turtlesim

```bash
ros2 run turtlesim turtlesim_node
```

## Run Nodes

```bash
ros2 run my_turtle_package move_turtle
ros2 run my_turtle_package move_circle
ros2 run my_turtle_package move_triangle
ros2 run my_turtle_package move_to_location
```

## Reset

```bash
ros2 service call /reset std_srvs/srv/Empty
```

## Work Completed

- Created a Python ROS 2 package.
- Published velocity commands to `/turtle1/cmd_vel`.
- Implemented circular, triangular, and target-based movement.
- Practiced rebuilding and sourcing after code changes.

## Result

The custom nodes successfully controlled Turtlesim. This lab improved my understanding of ROS 2 package structure, node execution, and velocity-based robot motion.
