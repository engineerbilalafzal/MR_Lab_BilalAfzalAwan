# Week 2: Turtlesim, Topics, Services, and RQT

## Aim

This lab introduced ROS 2 command-line tools using Turtlesim. I practiced launching nodes, controlling a simulated turtle, publishing topic messages, calling services, and using RQT to inspect the running ROS graph.

## Commands

Start Turtlesim:

```bash
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtlesim_node
```

Keyboard control:

```bash
source /opt/ros/humble/setup.bash
ros2 run turtlesim turtle_teleop_key
```

Inspect topics:

```bash
ros2 topic list
ros2 topic echo /turtle1/pose
```

Publish velocity:

```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"
```

Call services:

```bash
ros2 service call /reset std_srvs/srv/Empty
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: 'turtle2'}"
ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 2.0, y: 8.0, theta: 1.57}"
```

Control second turtle:

```bash
ros2 topic pub /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.5}, angular: {z: 1.0}}"
```

Open RQT:

```bash
rqt
```

## Observations

Topics continuously stream data, while services perform request-response actions. Spawning a second turtle created separate pose and velocity topics, showing how independent robots can be controlled in the same ROS 2 system.

## Result

I controlled Turtlesim through keyboard input, topic publishing, service calls, and RQT. The lab clarified the practical difference between topics and services.
