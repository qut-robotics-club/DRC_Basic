# DRC_Basic
This is a basic setup for teams competing in the 2020 virtual Droid Racing Competition. To help us set this up, we have used a differential setup available here: https://github.com/richardw05/mybot_ws.

The system seems to be slightly buggy at the moment, and early attempts to modify it into a ackermann drive setup made it a lot worse. Will update when solved.
# Installation
This should work for the virtual machine from https://www.mathworks.com/robotics/v3/ros_vm_install. Other systems may need you to run a catkin_make command to get the file paths
sorted

Copy the drc_ws folder into the home directory. Copy the track_layout folder into ~/.gazebo/worlds.
Open a terminal and run:
echo "source ~/mybot_ws/devel/setup.bash" >> ~/.bashrc
echo "source ~/drc_ws/devel/setup.bash" >> ~/.bashrc

# Running
A minimal example has been set up that moves the cart in a circle if it is recieving images properly.
Run the command "/home/user/mybot_ws/run_gazebo.sh" to open a gazebo environment with the cart and a VERY temporary track.
Run the command "rosrun basic talker.py" to run the basic node that will move the cart.
The sample code that gets a camera image and causes movement can be found at ~/drc_ws/src/basic/scripts/talker.py.
Modifying the image_callback function should allow you to do your own navigation.