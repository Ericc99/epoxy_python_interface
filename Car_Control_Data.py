from squaternion import Quaternion
from math import asin, atan2
# Location Data Structure
class Location():
    def __init__(self):
        # Activation 
        self.activated = False

        # Time:
        self.time = Time_Stamp()

        # Orientation Data: Megnatic Sensor
        self.orientation = Orientation_Status()

        # Linear Acceleration
        self.lin_acc = Linear_Acc()

        # Linear Velocity
        self.lin_vel = Linear_Vel()

        # Realtive Location
        self.loc_x = 0
        self.loc_y = 0
        self.loc_z = 0

        # Angular Velocity
        self.ang_vel = Angular_Vel()
    
    def Update(self, imu):
        # First time plugin data
        if self.activated == False:
            # Data type of Time: from genpy.rostime import Time
            self.time.Init(imu.header.stamp.secs, imu.header.stamp.nsecs)
            self.activated = True
        # Normal Updates
        # Time Update
        self.time.Update(imu.header.stamp.secs, imu.header.stamp.nsecs)
        # Orientation Update
        self.orientation.Update(imu.orientation.w, imu.orientation.x, imu.orientation.y, imu.orientation.z)
        # Angular Velocity Update
        self.ang_vel.Update(imu.angular_velocity.x, imu.angular_velocity.y, imu.angular_velocity.z)
        # Linear Acceleration Update
        self.lin_acc.Update(imu.linear_acceleration.x, imu.linear_acceleration.y, imu.linear_acceleration.z)
    
    def Calculate_Vel(self):
        pass

    
    def Print(self):
        display = 'Status:\n' + str(self.time.Print()) + str(self.orientation.Print()) + str(self.ang_vel.Print()) + str(self.lin_acc.Print())
        # display = str(self.time.Print())

        return display

# Linear Velocity Data Structure
class Linear_Vel():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def Update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def Print(self):
        display = 'Linear Velocity: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
        return display

# Linear Acceleration Data Structure
class Linear_Acc():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def Update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Print(self):
        display = 'Linear Acceleration: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
        return display

# Angular Acceleration Data Structure
class Angular_Vel():
    # Unit of Angular Velocity is Rad/Sec
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
    
    def Update(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def Print(self):
        display = 'Angular Velocity: \n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
        return display


# Orientation Data Structure
class Orientation_Status():
    def __init__(self):
        # This x, y, z refer to the euler angles but not the quaternions
        self.x = 0
        self.y = 0
        self.z = 0
    
    # Input quaternions and record eulers
    def Update(self,w, x, y, z):
        # pitch = asin(-2 * q1 * q3 + 2 * q0* q2)
        # roll  = atan2(2 * q2 * q3 + 2 * q0 * q1, -2 * q1 * q1 - 2 * q2* q2 + 1)
        # yaw   = atan2(2*(q1*q2 + q0*q3),q0*q0+q1*q1-q2*q2-q3*q3)


        quanternion = Quaternion(w, x, y, z)
        euler = quanternion.to_euler(degrees=True)
        self.x = euler[0]
        self.y = euler[1]
        self.z = euler[2]

        # self.z = yaw
        # self.x = roll
        # self.y = pitch
    
    # Display Orientation Info
    def Print(self):
        display = 'Orientation:\n' + 'x: ' + str(self.x) + ' \ny: ' + str(self.y) + ' \nz: ' + str(self.z) + '\n'
        return display
        

# Time Stamp Data Structure
class Time_Stamp():
    def __init__(self):
        self.start = Instance()
        self.now = Instance()

    # Init Time Stamp, set start time
    def Init(self, sec, nsec):
        self.start.Update(sec, nsec)
        self.now.Update(sec, nsec)

    # Update time stamp, update now
    def Update(self, sec, nsec):
        self.now.Update(sec, nsec)

    # Calculate time since start
    def Duration(self):
        delta_nsec = self.now.nsec - self.start.nsec
        delta_sec = self.now.sec - self.start.sec
        if delta_nsec < 0:
            delta_sec = delta_sec -1
            delta_nsec = delta_nsec + 1000000000
        
        return [delta_sec, delta_nsec]
    
    # Dispaly Time Info
    def Print(self):
        display = 'Time: \n' + 'Starting Time: \n' + self.start.Print() + 'Now: \n' + self.now.Print() + 'Duration: ' + str(self.Duration()) + '\n'
        return display

# Time Instances
class Instance():
    def __init__(self):
        self.sec = 0
        self.nsec = 0
    
    # Update the time instance data
    def Update(self, sec, nsec):
        self.sec = sec
        self.nsec = nsec

    # Display Instance Info
    def Print(self):
        display = 'sec: ' + str(self.sec) + ' nsec: ' + str(self.nsec) + '\n'
        return display




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
