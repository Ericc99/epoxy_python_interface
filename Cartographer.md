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

Then you can run the following shell file to install the abseil-cpp library manually.

```
src/cartographer/scripts/install_abseil.sh
```

Now you can build it using ninja, it si significantly faster than make.

```
catkin_make_isolated --install --use-ninja
```

欸嘿然后你就报错了，看起来还是个无关痛痒的东西，欸嘿就是玩，气不气。

This error might be caused by some missing packagaes or wrong versions of some pacakages. In my case it is Sphinx.

After searching I found that my Sphinx is out of date and an API of nijna2 it is still using has been abandoned. The problem is addressed [here](https://www.cnblogs.com/havain/p/16377674.html).

Then all you have to do is to upgrade Sphinx.

```
pip install Sphinx --upgrade
```

然后就没有包的问题了，就出现了更奇怪的C object无法编译
