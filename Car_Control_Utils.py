import rospy, threading, time
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from Car_Control_Data import patterns as preset_data
from Car_Control_Data import paints as paint_patterns
# from Car_Control_Data import Location
# from sensor_msgs.msg import Imu
import datetime as dt

import io
import sys

# Modify buffer of print function
# sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer, 100000))

class CarControl():
    def __init__(self):
        # Define some global variables around the whole class
        # Moving status of the whole car
        self.moving = False
        # ROS topic publisher towards the car control topic 'cmd_vel'
        self.publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        # Init the speed of the car
        self.speed = [0, 0, 0, 0]
        self.running = False
        self.thread = None
        self.listening = False
        self.subscriber = None
        self.movements = None
        self.counter = 0
        self.location = None
        self.time = time.time()
        self.pump_controller = rospy.Publisher('toggle',String, queue_size=10)
        self.pump_thread = None
        self.pumping = False
        self.pump_trigger = False
        self.painting = False
    
    # Function start, first to call after the __init__ function to start essentail things for the class and ROS
    # Can only be called once
    def start(self):
        if not self.running:
            # Init ROS node
            rospy.init_node('Car_Control')
            # Init the publisher thread
            self.thread = threading.Thread(target=self.publish, args=[])
            # Set as daemon thread to end with the main thread
            self.thread.setDaemon(True)
            # Start the thread
            self.thread.start()
            # Init pump publisher thread
            self.pump_thread = threading.Thread(target=self.pump_publisher, args=[])
            # Set as daemon thread to end with the main thread
            self.pump_thread.setDaemon(True)
            # Start the thread
            self.pump_thread.start()
            # Change the running status to True
            self.running = True
            # # Status of listener
            # self.listening = False
            # # Start the listener thread
            # self.subscriber = rospy.Subscriber('/imu', Imu, self.listen, queue_size=1000)
            # # Construct the Location data structure without init
            # self.location = Location()

        else:
            pass

    # Pump publisher function
    def pump_publisher(self):
        while True:
            if self.pump_trigger:
                print('Pumping triggered')
                # Construct a data structure to pass to pump
                string = String()
                if self.pumping:
                    string.data = 'H'
                    print('Pump status updated to: open')
                else:
                    string.data = 'G'
                    print('Pump status updated to: close')
                self.pump_controller.publish(string)
                self.pump_trigger = False
            else:
                pass

    # Publisher that runs inside of the child thread, listen to the information of main loop and publish it to the car
    def publish(self):
        while True:
            if self.moving:
                # print('Publishing')
                print('\n')
                print(dt.datetime.now())
                # Construct a data structure to pass to cmd_vel
                twist = Twist()
                twist.linear.x = self.speed[0]
                twist.linear.y = self.speed[1]
                twist.linear.z = self.speed[2]
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = self.speed[3]
                # Print speed data
                print('Speed: ' + str(self.speed))
                # Publish the data to car
                self.publisher.publish(twist)
                # Command is being passed at a rate of 5Hz
                time.sleep(0.2)
            else:
                # If not moving then just wait for update
                pass
    
    # Update function used by main loop to modify the parameters
    def update(self, moving, speed):
        self.moving = moving
        for i in range(4):
            # Force format conversion in case there is anything wrong
            self.speed[i] = float(speed[i])
    
    def paintStatus(self, paint):
        if self.painting == paint:
            print('Painting status remains ' + str(paint))
        else:
            self.paintTrigger(paint)
            print('Painting status updated to ' + str(paint) + ' from ' + str(self.painting))
            self.painting = paint
        
        

    # Several default modes to go according to the predefined mode
    def default(self, pattern):
        usr_in = int(pattern)
        if usr_in >= 1 and usr_in <= len(preset_data) - 1:
            preset = preset_data[int(usr_in)]
            print(preset.name)
            for i in range(len(preset.delay)):
                if i < len(preset.delay) - 1:
                    self.update(True, preset.speed[i])
                else:
                    self.update(False, preset.speed[i])
                time.sleep(preset.delay[i])
        else:
            pass
        
    def paintDefault(self, num):
        num = int(num)
        if num >= 1 and num <= len(paint_patterns) - 1:
            pattern = paint_patterns[num]
            print(pattern.name)
            for i in range(len(pattern.delay)):
                if i < len(pattern.delay) - 1:
                    self.update(True, pattern.speed[i])
                    self.paintStatus(pattern.paint[i])
                else:
                    self.update(False, pattern.speed[i])
                    self.paintStatus(pattern.paint[i])
                time.sleep(pattern.delay[i])
        else:
            pass
    
    def paintTrigger(self, status):
        if status:
            self.pumping = True
            self.pump_trigger = True
        else:
            self.pumping = False
            self.pump_trigger = True


    
    # # Listener towards the IMU data
    # def listen(self, imu):
    #     if self.listening == True:
    #         # Retrive the orientation data in the format of Quanternion
    #         # Data comes from the Megnatic sensor within the IMU module
    #         # self.time = time.time()
    #         self.location.Update(imu)
    #         self.location.Calculate_Vel()
    #         self.location.Calculate_Dis()
    #         # print('update:', time.time() - self.time)
    #         # self.time = time.time()
    #         # with open('./Log.txt', 'a') as f:
    #             # if self.counter % 50 == 0:
    #         # rospy.loginfo(str(self.location.Print()))
    #         # print(str(self.location.Print()), flush=True)
    #             # print(str(self.location.Print()), file=f)
    #             # self.counter += 1
    #         # print('print', time.time() - self.time)
    #     else:
    #         pass

    # Run function for the mainloop
    def run(self):
        print('------Program Begins------')
        control = self
        control.start()
        while True:
            usr_in = input('Command: ')
            if usr_in == '0':
                print('------Program Terminated------')
                break
            elif usr_in == '1':
                # Default moving mode speed 0.154 forward 1s
                speed =  [0.154, 0, 0, 0]
                control.update(True, speed)
                time.sleep(1)
                speed =  [0, 0, 0, 0]
                control.update(False, speed)
            elif usr_in == '2':
                tmp = input('Command Intro: ' + preset_data[0])
                control.default(tmp)
            elif usr_in == '3':
                # if self.listening == True:
                #     print('---Stopped Listening---')
                #     self.listening = False
                # else:
                #     print('---Started Listening---')
                #     self.listening = True
                print('IMU funtion has been disabled... for now.')
            elif usr_in == '4':
                tmp = input('H for start pumping, G for stop pumping')
                if tmp == 'H':
                    self.paintTrigger(True)
                    # self.pumping = True
                    # self.pump_trigger = True
                elif tmp == 'G':
                    self.paintTrigger(False)
                    # self.pumping = False
                    # self.pump_trigger = True
                else:
                    print('Command not found...')
                print('Hihihi')
            elif usr_in == '5':
                tmp = input('Command Intro: ' + paint_patterns[0])
                control.paintDefault(tmp)

            else:
                pass
            # print('Testing')


    
if __name__ == '__main__':
    control = CarControl()
    control.run()







