# ROS

## Discriptions

This directory is designed for the ROS implementation of Construction Robotics. The major contributor is Eric CUI.

## Usage

1. ROS Tracer Setup
   * Start ROS Core service

    ```
    roscore
    ```

   * Source the right ROS setup.bash

    ```
    cd devel
    source setup.bash
    ```
   
   * First time use tracer-ros package

    ```
    rosrun tracer_bringup setup_can2usb.bash
    ```

    * Not the first time use tracer-ros package

    ```
    rosrun tracer_bringup bringup_can2usb.bash
    ```

    * Start the base node for the robot within CAN

    ```
    roslaunch tracer_bringup tracer_robot_base.launch
    ```

    * Start keyboard control

    ```
    roslaunch tracer_bringup tracer_teleop_keyboard.launch
    ```

2. IMU Module Setup
   * Check USB Port

    ```
    ls -l /dev/ttyUSB*
    ```

    * Authorize usage of the port

    ```
    sudo chmod 666 /dev/ttyUSB0
    ```

    * Start the node service

    ```
    roslaunch fdilink_ahrs ahrs_data.launch
    ```

    * Essential data packages

    ```
    Detail reference can be seen within the Imu class of sensor_msgs.msg
    ```

   
