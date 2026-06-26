# Week 8: Robot Description and RViz Visualization

## Aim

This lab focuses on URDF/Xacro robot modeling and visualization in RViz. The package `my_robot_description` contains a robot model, mesh files, RViz configuration, and a launch file that starts the required publishers.

## Package

```text
my_robot_description
```

## Build

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
colcon build --packages-select my_robot_description
source install/setup.bash
```

## Run

```bash
ros2 launch my_robot_description display.launch.py
```

The launch file starts:

- `robot_state_publisher`
- `joint_state_publisher`
- `rviz2`

## Files

```text
urdf/my_robot.urdf
urdf/custom_robot.urdf
urdf/vista_robot.urdf.xacro
meshes/*.STL
launch/display.launch.py
rviz/robot.rviz
```

## RViz Setup

Use:

```text
Fixed Frame: base_link
RobotModel: /robot_description
TF: enabled
```

If RViz opens with a duplicate RobotModel display, remove the red/error one and keep the display that shows `Status: Ok`.

## Notes

The workspace path contains a space (`mr labs`), so the launch file quotes the Xacro model path before passing it to `xacro`. The robot materials were also made brighter to make the model easier to see in RViz.

## Useful Commands

```bash
ros2 topic echo /robot_description --once
ros2 run tf2_tools view_frames
```

## Result

The robot description is published to `/robot_description`, transforms are available on `/tf`, and the model can be visualized in RViz.
