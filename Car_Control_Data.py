class Moving_Preset_Pattern():
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.delay = None

    def Set_Speed(self, speed):
        self.speed = speed
    
    def Set_Delay(self, delay):
        self.delay = delay

class Location_Info():
    def __init__(self):
        # Orientation Data: Megnatic Sensor
        self.orientation_x = 0
        self.orientation_y = 0
        self.orientation_z = 0

        # 
        self.dis_x = 0
        self.dis_y = 0
        self.dis_z = 0

        self.ang_x = 0
        self.ang_y = 0
        self.ang_z = 0

        self.lin_vel_x = 0
        self.lin_vel_y = 0
        self.lin_vel_z = 0

        self.ang_vel_x = 0
        self.ang_vel_y = 0
        self.ang_vel_z = 0

    # Function to make adjustment and calabration
    def calabrate(self):
        pass

    # Function to calculate and update the data
    def Update(self):
        pass

    # Function to clear the data frame
    def Clear(self):
        pass



pattern_intro = '''
Pattern 1: Forward 1m
Pattern 2: 90 Degrees Left
Pattern 3: Backward 1m
Pattern 4: 90 Degrees Right
Pattern 5: 3m Forward
Pattern 6: Full Set
'''

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


patterns = [pattern_intro, pattern1, pattern2, pattern3, pattern4, pattern5, pattern6, pattern7]
