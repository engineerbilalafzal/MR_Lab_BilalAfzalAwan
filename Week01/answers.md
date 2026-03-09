answers
Node
A node is a small program in ROS 2 that performs a specific task and can communicate with other nodes.

Topic
A topic is a named channel where nodes send and receive messages between each other.

Package
A package is a folder that contains ROS 2 code, configuration files, and other resources for a project.

Workspace
A workspace is a main directory where multiple ROS 2 packages are developed and built together.

Why sourcing is required
Sourcing sets up the ROS 2 environment so the system can locate your packages and executables. If you don’t source the workspace, ROS 2 commands will not recognize your custom packages.

Purpose of colcon build
colcon build is used to build and compile all packages in the workspace.

Entry_points console script in setup.py
The entry_points console script creates a command that lets you run your Python node easily using ros2 run, which then calls the main() function in that file.

Publisher–Subscriber Diagram

[Publisher Node] ---> (Topic) ---> [Subscriber Node]

The publisher node sends messages to a topic, and the subscriber node receives those messages from the same topic.