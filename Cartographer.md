# Notes for Cartographer

Github Link: [Cartographer](https://github.com/cartographer-project)

## Setup Guide

With proper ROS env setted up can one easily setup cartographer with the following commands.

First install WSTools

```
sudo apt-get update
sudo apt-get install -y python3-wstool python3-rosdep ninja-build stow
```

Then create your own file directory for cartographer

```
mkdir catkin_ws
cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src
```

Now you can use rosdep to install some dependencies, first line is package check, might give an error due to packages existence, just ignore it.

```
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
```

Last line is to install all packages according to the package.xml file. Might give out an error due to package overlapping. Solution can be found here [Solution](https://github.com/cartographer-project/cartographer_ros/issues/1726)

