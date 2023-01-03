class Moving_Preset_Pattern():
    def __init__(self, name):
        self.name = name
        self.speed = None
        self.delay = None

    def Set_Speed(self, speed):
        self.speed = speed
    
    def Set_Delay(self, delay):
        self.delay = delay

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

