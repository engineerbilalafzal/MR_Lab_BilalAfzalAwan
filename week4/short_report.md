# Week 4 Short Report

## Approach

I used a launch file to start the Turtlesim environment and handle multiple nodes from one command. The setup created two turtles and allowed separate velocity topics for each one. I then ran the `follow_leader` node, which subscribes to pose data and publishes commands to make the second turtle follow the first.

## Data Recording

Rosbag was used to record pose and velocity topics:

```text
/turtle1/pose
/turtle1/cmd_vel
/turtle2/pose
/turtle2/cmd_vel
```

A recorded run was saved at:

```bash
src/week4/rosbag2_recordings/week4_demo_20260626_184334
```

The bag contained 1248 messages and was checked with `ros2 bag info`.

## Observations

- The launch system reduced the number of manual terminal commands.
- The follower turtle reacted to pose changes from the leader.
- A small delay was visible because pose messages and velocity commands are processed at a finite rate.
- RQT Plot helped compare velocity command values over time.

## Conclusion

This lab connected launch files, multi-node execution, topic recording, and data visualization. It showed how ROS 2 tools can be combined to test and analyze a robot behavior.
