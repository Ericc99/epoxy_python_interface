import rospy, threading, time
from geometry_msgs.msg import Twist
from Car_Control_Data import patterns as preset_data

class CarControl():
    def __init__(self):
        # Define some global variables around the whole class
        self.moving = False
        self.publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.speed = [0, 0, 0, 0]
        self.running = False
        self.thread = None
    
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
            # Change the running status to True
            self.running = True
        else:
            pass

    # Publisher that runs inside of the child thread, listen to the information of main loop and publish it to the car
    def publish(self):
        while True:
            if self.moving:
                print('Publishing')
                # Construct a data structure to pass to cmd_vel
                twist = Twist()
                twist.linear.x = self.speed[0]
                twist.linear.y = self.speed[1]
                twist.linear.z = self.speed[2]
                twist.angular.x = 0
                twist.angular.y = 0
                twist.angular.z = self.speed[3]
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
                tmp = input('Command: ' + preset_data[0])
                control.default(tmp)


    
if __name__ == '__main__':
    control = CarControl()
    control.run()







