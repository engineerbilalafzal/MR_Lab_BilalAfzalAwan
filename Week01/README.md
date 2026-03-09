Brief Description

In Week 1 lab, we learned the basics of Linux and ROS 2. We set up a ROS 2 workspace, created our first Python package, and added a simple node that prints a message when it runs. The lab also introduced important ROS 2 concepts like nodes, topics, packages, and workspaces. After building the workspace, we successfully ran the node using a ROS 2 command.

Commands Used

Verify ROS 2 installation

echo $ROS_DISTRO

Source ROS 2 environment

source /opt/ros/humble/setup.bash

Create ROS 2 workspace

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

Build the workspace

colcon build

Source the workspace

source install/setup.bash

Make sourcing persistent

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc
source ~/.bashrc

Create Python package

cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python <package_name>

Build and source package

cd ~/ros2_ws
colcon build
source install/setup.bash

List packages

ros2 pkg list

Make node file executable

chmod +x <node_file>.py

Run the node

ros2 run <package_name> <node_name>
Problems Faced and How They Were Solved

Problem: ros2: command not found
Solution: The ROS 2 environment was not sourced, so sourcing the setup file fixed the issue.

Problem: Package not appearing in the package list
Solution: Rebuilt the workspace and sourced the install setup file again.

Problem: Node not running with the run command
Solution: Added the node in setup.py under entry_points and rebuilt the workspace.

Problem: Small Python syntax errors in the node file
Solution: Checked indentation and imports, then rebuilt and sourced the workspace again.

Reflection

This lab helped me understand how to use Linux commands and manage a ROS 2 workspace. I learned how to create a package and run a simple node. I also understood why sourcing the workspace is important for ROS 2 to detect packages. Solving small errors during the process also improved my debugging skills. Overall, it was a good introduction to ROS 2 development.
