from math import asin, atan2, cos, sin, radians, degrees
import numpy

# # Location Data Structure
# class Location():
#     def __init__(self):
#         # Activation 
#         self.activated = False

#         # Time:
#         self.time = Time_Stamp()

#         # Orientation Data: Megnatic Sensor
#         self.orientation = Orientation_Status()

#         # Linear Acceleration
#         self.lin_acc = Linear_Acc()

#         # Linear Velocity
#         self.lin_vel = Linear_Vel()

#         # Adjustment of Linear Velocity
#         self.count = 0
#         self.tot_x = 0
#         self.tot_y = 0
#         self.tot_z = 0
#         self.adj_x = 0
#         self.adj_y = 0
#         self.adj_z = 0

#         # Realtive Location
#         self.loc_x = 0
#         self.loc_y = 0
#         self.loc_z = 0

#         # Angular Velocity
#         self.ang_vel = Angular_Vel()
    
#     def Update(self, imu):
#         # First time plugin data
#         if self.activated == False:
#             # Data type of Time: from genpy.rostime import Time
#             self.time.Init(imu.header.stamp.secs, imu.header.stamp.nsecs)
#             self.activated = True
#         # Normal Updates
#         # Time Update
#         self.time.Update(imu.header.stamp.secs, imu.header.stamp.nsecs)
#         # Orientation Update
#         self.orientation.Update(imu.orientation.w, imu.orientation.x, imu.orientation.y, imu.orientation.z)
#         # Angular Velocity Update
#         self.ang_vel.Update(imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z)
#         # Linear Acceleration Update
#         self.lin_acc.Update(imu.linear_acceleration.x, imu.linear_acceleration.y, imu.linear_acceleration.z)
    
#     def Calculate_Vel(self):
#         r = radians(self.orientation.x)
#         p = radians(self.orientation.y)
#         y = radians(self.orientation.z)

#         M_x = numpy.array([[1, 0, 0], 
#         [0, cos(r), sin(r)],
#         [0, -sin(r), cos(r)]]
#         )

#         M_y = numpy.array([[cos(p), 0, -sin(p)], 
#         [0, 1, 0],
#         [sin(p), 0, cos(p)]]
#         )

#         M_z = numpy.array([[cos(y), sin(y), 0], 
#         [-sin(y), cos(y), 0],
#         [0, 0, 1]]
#         )

#         X_x = self.lin_acc.x
#         X_y = self.lin_acc.y
#         X_z = self.lin_acc.z

#         X = numpy.array([[X_x], [X_y], [X_z]])

#         tmp = numpy.dot(numpy.linalg.inv(M_x), X)
#         tmp = numpy.dot(numpy.linalg.inv(M_y), tmp)
#         G = numpy.dot(numpy.linalg.inv(M_z), tmp)
#         G = G - numpy.array([[0], [0], [9.80665]])
#         G = G + numpy.array([[-0.236], [-0.123], [0.0786]])
#         # print(G[0], G[1], G[2])

#         # For data adjustment
#         self.lin_vel.Update(G[0], G[1], G[2])
#         self.tot_x += G[0]
#         self.tot_y += G[1]
#         self.tot_z += G[2]
#         self.count += 1
#         self.adj_x = self.tot_x / self.count
#         self.adj_y = self.tot_y / self.count
#         self.adj_z = self.tot_z / self.count

#         # print(self.count)
#         print(self.adj_x, self.adj_y, self.adj_z)

#     def Calculate_Dis(self):
#         delta_time = self.time.Gap()
#         self.loc_x += self.lin_vel.x * delta_time
#         self.loc_y += self.lin_vel.y * delta_time
#         self.loc_z += self.lin_vel.z * delta_time
#         duration = self.time.Duration()
#         dur_num = duration[0] + duration[1] / 1000000000
#         # print(dur_num)
#         # print(self.loc_x, self.loc_y, self.loc_z)



    
#     def Print(self):
#         display = 'Status:\n' + str(self.time.Print()) + str(self.orientation.Print()) + str(self.ang_vel.Print()) + str(self.lin_acc.Print())
#         # display = str(self.time.Print())

#         return display

# # Linear Velocity Data Structure
# class Linear_Vel():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.z = 0
    
#     def Update(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def Print(self):
#         display = 'Linear Velocity: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
#         return display

# # Linear Acceleration Data Structure
# class Linear_Acc():
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.z = 0
    
#     def Update(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def Print(self):
#         display = 'Linear Acceleration: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
#         return display

# # Angular Acceleration Data Structure
# class Angular_Vel():
#     # Unit of Angular Velocity is Rad/Sec
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.z = 0
    
#     def Update(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
    
#     def Print(self):
#         display = 'Angular Velocity: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
#         return display


# # Orientation Data Structure
# class Orientation_Status():
#     def __init__(self):
#         # This x, y, z refer to the euler angles but not the quaternions
#         self.x = 0
#         self.y = 0
#         self.z = 0
    
#     # Input quaternions and record eulers
#     def Update(self,w, x, y, z):
#         q0 = w
#         q1 = x
#         q2 = y
#         q3 = z
#         # This Calculation Method is in the rotation order of Z-Y-X
#         # Tool to check is here: https://www.andre-gaschler.com/rotationconverter/
#         pitch = degrees(asin(-2 * q1 * q3 + 2 * q0* q2))
#         roll  = degrees(atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1))
#         yaw   = degrees(atan2(2*(q1*q2 + q0*q3),q0*q0+q1*q1-q2*q2-q3*q3))

#         self.x = roll
#         self.y = pitch
#         self.z = yaw
    
#     # Display Orientation Info
#     def Print(self):
#         display = 'Orientation:\n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
#         return display
        

# # Time Stamp Data Structure
# class Time_Stamp():
#     def __init__(self):
#         self.start = Instance()
#         self.now = Instance()
#         self.previous = Instance()

#     # Init Time Stamp, set start time
#     def Init(self, sec, nsec):
#         self.start.Update(sec, nsec)
#         self.now.Update(sec, nsec)
#         self.previous.Update(sec, nsec)

#     # Update time stamp, update now
#     def Update(self, sec, nsec):
#         self.previous.Update(self.now.sec, self.now.nsec)
#         self.now.Update(sec, nsec)

#     # Calculate time since start
#     def Duration(self):
#         delta_nsec = self.now.nsec - self.start.nsec
#         delta_sec = self.now.sec - self.start.sec
#         if delta_nsec < 0:
#             delta_sec = delta_sec -1
#             delta_nsec = delta_nsec + 1000000000
        
#         return [delta_sec, delta_nsec]
#     # Calculate the time interval of single measurement
#     def Gap(self):
#         delta_nsec = self.now.nsec - self.previous.nsec
#         delta_sec = self.now.sec - self.previous.sec
#         if delta_nsec < 0:
#             delta_sec = delta_sec -1
#             delta_nsec = delta_nsec + 1000000000
        
#         delta = delta_sec + (delta_nsec / 1000000000)
#         return delta
    
#     # Dispaly Time Info
#     def Print(self):
#         display = 'Time: \n' + 'Starting Time: \n' + self.start.Print() + 'Now: \n' + self.now.Print() + 'Duration: ' + str(self.Duration()) + '\n'
#         return display

# # Time Instances
# class Instance():
#     def __init__(self):
#         self.sec = 0
#         self.nsec = 0
    
#     # Update the time instance data
#     def Update(self, sec, nsec):
#         self.sec = sec
#         self.nsec = nsec

#     # Display Instance Info
#     def Print(self):
#         display = 'sec: ' + str(self.sec) + ' nsec: ' + str(self.nsec) + '\n'
#         return display




# Routing Pattern Data Structure
class Moving_Preset_Pattern():
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.delay = None

    def Set_Speed(self, speed):
        self.speed = speed
    
    def Set_Delay(self, delay):
        self.delay = delay


# Pattern Intro Message
pattern_intro = '''
Pattern 1: Forward 1m
Pattern 2: 90 Degrees Left
Pattern 3: Backward 1m
Pattern 4: 90 Degrees Right
Pattern 5: 3m Forward
Pattern 6: Full Set
'''

# Pattern definitions
pattern1 = Moving_Preset_Pattern('Forward 1m')
speed1 = [
    [0.03, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.154, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.03, 0, 0, 0],
    [0, 0, 0, 0]
]
delay1 = [0.2, 0.2, 0.2, 0.2, 5.5, 0.2, 0.2, 0.2, 0.2, 0]
pattern1.Set_Speed(speed1)
pattern1.Set_Delay(delay1)

pattern2 = Moving_Preset_Pattern('90 Degrees Left')
speed2 = [
    [0,0,0,0.5],
    [0,0,0,0]
]
delay2 = [3.2, 0]
pattern2.Set_Speed(speed2)
pattern2.Set_Delay(delay2)

pattern3 = Moving_Preset_Pattern('Backward 1m')
speed3 = [
    [-0.03, 0, 0, 0],
    [-0.06, 0, 0, 0],
    [-0.09, 0, 0, 0],
    [-0.12, 0, 0, 0],
    [-0.154, 0, 0, 0],
    [-0.12, 0, 0, 0],
    [-0.09, 0, 0, 0],
    [-0.06, 0, 0, 0],
    [-0.03, 0, 0, 0],
    [0, 0, 0, 0]
]
delay3 = [0.2, 0.2, 0.2, 0.2, 5.5, 0.2, 0.2, 0.2, 0.2, 0]
pattern3.Set_Speed(speed3)
pattern3.Set_Delay(delay3)

pattern4 = Moving_Preset_Pattern('90 Degrees Right')
speed4 = [
    [0,0,0,-0.49],
    [0,0,0,0]
]
delay4 = [3, 0]
pattern4.Set_Speed(speed4)
pattern4.Set_Delay(delay4)

pattern5 = Moving_Preset_Pattern('Forward 3m')
speed5 = [
    [0.03, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.154, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.03, 0, 0, 0],
    [0, 0, 0, 0]
]
delay5 = [0.2, 0.2, 0.2, 0.2, 20, 0.2, 0.2, 0.2, 0.2, 0]
pattern5.Set_Speed(speed5)
pattern5.Set_Delay(delay5)

pattern7 = Moving_Preset_Pattern('Forward 0.5m')
speed7 = [
    [0.03, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.154, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.03, 0, 0, 0],
    [0, 0, 0, 0]
]
delay7 = [0.2, 0.2, 0.2, 0.2, 1, 0.2, 0.2, 0.2, 0.2, 0]
pattern7.Set_Speed(speed7)
pattern7.Set_Delay(delay7)

pattern_delay = Moving_Preset_Pattern('Stop 1s')
speed_delay = [
    [0, 0, 0, 0]
]
delay_delay = [1]
pattern_delay.Set_Speed(speed_delay)
pattern_delay.Set_Delay(delay_delay)

pattern6 = Moving_Preset_Pattern('Full Set')
speed6 = speed5 + speed_delay + speed2 + speed1 + speed2 + speed7 + speed_delay + speed5
delay6 = delay5 + delay_delay + delay2 + delay1 + delay2 + delay7 + delay_delay + delay5
pattern6.Set_Speed(speed6)
pattern6.Set_Delay(delay6)

# Pattern list, need to register all useful patterns
patterns = [pattern_intro, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7]


# Routing with Painting Pattern Data Structure
class Integrated_Pattern():
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.delay = None
        self.paint = None

    def Set_Speed(self, speed):
        self.speed = speed
    
    def Set_Delay(self, delay):
        self.delay = delay
    
    def Set_Paint(self, paint):
        self.paint = paint

# Pattern Intro Message
paint_intro = '''
Paint 1: Paint a 1m pathway
'''

paint1 = Integrated_Pattern('Forward 1m')
paint_s1 = [
    [0.03, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.154, 0, 0, 0],
    [0.12, 0, 0, 0],
    [0.09, 0, 0, 0],
    [0.06, 0, 0, 0],
    [0.03, 0, 0, 0],
    [0, 0, 0, 0]
]
paint_d1 = [0.2, 0.2, 0.2, 0.2, 5.5, 0.2, 0.2, 0.2, 0.2, 0]
painting1 = [True, True, True, True, True, True, True, True, True, False]

paint1.Set_Speed(paint_s1)
paint1.Set_Delay(paint_d1)
paint1.Set_Paint(painting1)

paints = [paint_intro, paint1]