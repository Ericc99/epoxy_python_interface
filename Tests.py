# To Operate Some Tests.
from math import cos

class Time_Stamp():
    def __init__(self):
        self.sec = 0
        self.nsec = 0
    
    def Modify(self, sec, nsec):
        self.sec = sec
        self.nsec = nsec
    
    def TimeSinceStart(self, start_time):
        delta_sec = self.sec - start_time.sec
        delta_nsec = self.nsec - start_time.nsec
        print(str(delta_sec) + str(delta_nsec))


if __name__ == '__main__':
    # start = Time_Stamp()
    # start.Modify(0, 0)
    # end = Time_Stamp()
    # end.Modify(10, 10)
    # end.TimeSinceStart(start)
    print(cos(90))
