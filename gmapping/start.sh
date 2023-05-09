#!/bin/bash
cd ~/Documents/ros_code
source devel/setup.bash
rosrun tracer_bringup bringup_can2usb.bash
roslaunch tracer_bringup tracer_robot_base.launch
ls -l /dev/ttyUSB*
sudo chmod 666 /dev/ttyUSB0
roslaunch lslidar_x10_driver lslidar_x10_serial.launch
sudo chmod 666 /dev/ttyUSB1
roslaunch fdilink_ahrs ahrs_data.launch
rostopic list
roslaunch my_slam_gmapping my_slam_gmapping.launch