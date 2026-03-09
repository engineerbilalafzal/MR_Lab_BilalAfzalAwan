Week 1 
Brief Description


Commands Used
Verify ROS 2 installation

echo $ROS_DISTRO
Source ROS 2 environment

source /opt/ros/humble/setup.bash
Create ROS 2 workspace

mkdir -p ~/ros2_ws_alishba/src cd ~/ros2_ws_alishba
Build the workspace

colcon build
Source the workspace

source install/setup.bash
Make sourcing persistent

echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc echo "source ~/ros2_ws_alishba/install/setup.bash" >> ~/.bashrc source ~/.bashrc
Create Python package

cd ~/ros2_ws_alishba/src ros2 pkg create --build-type ament_python my_first_pkg
Build and source package

cd ~/ros2_ws_alishba colcon build source install/setup.bash
List packages

ros2 pkg list | grep my_first_pkg
Make node file executable (optional but good practice)

chmod +x ~/ros2_ws_alishba/src/my_first_pkg/my_first_pkg/simple_node.py
Run the node

ros2 run my_first_pkg simple_node ros2 run my_first_pkg simple_node --ros-args -p student_name:=AlishbaKiyani
Problems Faced and How They Were Solved

    Problem: ros2: command not found Solution: ROS 2 environment was not sourced. Fixed by running source /opt/ros/humble/setup.bash.

    Problem: Package my_first_pkg not found in ros2 pkg list Solution: Ensured the package was created inside ~/ros2_ws_alishba/src, rebuilt workspace using colcon build, and sourced install/setup.bash.

    Problem: Node executable not found when running ros2 run Solution: Registered the node in setup.py under entry_points and rebuilt the workspace.

    Problem: Minor Python syntax errors in the node file Solution: Checked indentation, imports, and file naming; rebuilt and sourced workspace again.

Reflection

This lab helped me gain hands-on experience with Linux terminal commands and ROS 2 workspace management. I learned how ROS 2 nodes communicate through topics and how to create and organize packages. Registering a Python node as an executable using entry_points clarified how ROS 2 locates and runs code. I also understood the importance of sourcing the workspace to make ROS commands work. Troubleshooting errors such as missing packages and command not found improved my debugging skills. Overall, this lab built my confidence in setting up ROS 2 environments and running my first ROS 2 node. I am now ready to explore more advanced nodes and topics in upcoming labs.
