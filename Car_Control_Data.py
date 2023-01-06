class Moving_Preset_Pattern():
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.delay = None

    def Set_Speed(self, speed):
        self.speed = speed
    
    def Set_Delay(self, delay):
        self.delay = delay

pattern_intro = '''
Pattern 1: Forward 1m
Pattern 2: 90 Degrees Left
Pattern 3: Backward 1m
Pattern 4: 90 Degrees Right
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
    [0,0,0,0.49],
    [0,0,0,0]
]
delay2 = [3, 0]
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

patterns = [pattern_intro, pattern1, pattern2, pattern3, pattern4]
