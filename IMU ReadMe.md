
## fdilink的imu驱动包
Deta-10-ros-v0.0.1
### 依赖：
```bash
sudo apt install ros-melodic-serial
```

### 使用：  
因为这个launch文件当中涉及串口的调用，首先需要通过
```
ls -l /dev/ttyUSB*
```  
来查看一下当前系统在使用哪些串口，找到IMU的USB串口。
之后再在launch文件当中修改串口信息，并使用以下命令为串口授予权限。
```
sudo chmod 666 /dev/ttyUSB0
```
之后调用以下命令即可将IMU的检测程序跑起来。
```
roslaunch fdilink_ahrs ahrs_data.launch
```

ahrs_driver.launch
```
<launch>
  <node pkg="fdilink_ahrs" name="ahrs_driver" type="ahrs_driver" output="screen" >
    <!-- 是否输出debug信息 -->
    <param name="debug"  value="false"/>
    
    <!-- 串口设备，可通过rules.d配置固定 -->
    <param name="port"  value="/dev/ttyUSB0"/>
    <!-- <param name="port"  value="/dev/ttyTHS1"/> -->

    <!-- 波特率 -->
    <param name="baud"  value="921600"/>

    <!-- 发布的imu话题名 -->
    <param name="imu_topic"  value="/imu"/>
    
    <!-- 发布的imu话题中的frame_id -->
    <param name="imu_frame"  value="imu"/>

    <!-- 地磁北的yaw角 --> # 二维指北的朝向，北为0，逆时针增加，0~2π的取值范围。
    <param name="mag_pose_2d_topic"  value="/mag_pose_2d"/>

    <!-- 发布的数据基于不同设备有不同的坐标系   -->
    <param name="device_type"  value="1"/> <!-- 0: origin_data, 1: for single imu or ucar in ROS, 2:for Xiao in ROS -->
  </node>
</launch> 
```
  其中`device_type`：
  
  0. Deta-10的原始坐标系模式
  1. 单独imu的坐标系模式

调用的ahrs_driver节点会发布`sensor_msgs/Imu`格式的imu topic。
```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Quaternion orientation
  float64 x
  float64 y
  float64 z
  float64 w
float64[9] orientation_covariance
geometry_msgs/Vector3 angular_velocity
  float64 x
  float64 y
  float64 z
float64[9] angular_velocity_covariance
geometry_msgs/Vector3 linear_acceleration
  float64 x
  float64 y
  float64 z
float64[9] linear_acceleration_covariance
```
针对Imu格式数据包当中的信息组成的简要分析：

IMU的采样频率是100Hz，但是精度也就那样...

Header部分：

典型Header数据包模式如下

```
[INFO] [1673009010.572985]: seq: 786419
stamp: 
  secs: 1673009005
  nsecs: 308080626
frame_id: "gyro_link"

```
seq：本次IMU总共测量数据点个数

stamp：时间戳部分

--secs：当前秒数，1LSB代表1S

--nsecs：当前毫秒数，1MSB代表10mS

frame_id：可以在launch文档当中设置的一个ID

Orientation 部分：

典型Orientation数据包如下：

```
[INFO] [1673009736.253439]: x: -0.0002744543016889013
y: -0.0014057133812456512
z: -0.4135259091854096
w: 0.9104915261268616
```

此处的orientation指的是啥我也不知道。。。但是貌似是个四维度的表示方法，一个实数三个虚数。

Orientation Covariance 部分：

```
[INFO] [1673010787.428395]: (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
```

这是啥我也不知道，救命

Angular Velocity部分：

```
[INFO] [1673010930.188876]: x: 0.002969999797642231
y: -0.0017580523854121566
z: 0.000375481293303892
```

代表角速度，不过看起来测得相当不准...

Linear Acceleration 部分：
```
[INFO] [1673011172.161708]: x: -0.18261173367500305
y: -0.054627519100904465
z: 9.749401092529297
```
这一部分代表IMU检测到的线速度，看起来准确性还行，但是我感觉累积误差应该也会非常恐怖。

它和上面的角速度一样，数据类型都是geometry_msgs.msg.Vector3()，直接调用xyz应该就能够获取相应的数据。



也会发布`geometry_msgs/Pose2D`格式的二维指北角话题，话题名默认为`/mag_pose_2d`。
```
float64 x
float64 y
float64 theta  # 指北角
```

### 2020-1-15
  维护了文件注释。

### 2020-10-20
  添加了`device_type`参数，可以在`ahrs_data.launch`文件中指定设备类型，根据不同设备类型以不同的坐标系发布ROS的imu数据。
  其中：

  0. Deta-10的原始坐标系模式
  1. 单独imu的坐标系模式

### 2023-01-06
  Eric更新了文档
