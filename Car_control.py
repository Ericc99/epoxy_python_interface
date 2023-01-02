import threading
import rospy
import time
from geometry_msgs.msg import Twist

# Publish Function
# While loop to publish signal repeatedly to the car in a rate of 5Hz
def pub():
    while True:
        if pub_cmd == False:
            pass
        else:
            print('Publishing:')
            print('Linear: ' + str(speed[0]) + ' ' + str(speed[1]) + ' ' + str(speed[2]))
            print('Angular: 0 0 ' + str(speed[3]))
            move()
            time.sleep(0.2)

# Moving Function
# Publihser to publish a single movement signal
def move():
    twist = Twist()
    twist.linear.x = speed[0]
    twist.linear.y = speed[1]
    twist.linear.z = speed[2]
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = speed[3]

    publisher.publish(twist)

def mover(duration, parameters):
    pass



if __name__ == '__main__':
    # Global Varibales
    global pub_cmd
    global publisher
    global speed
    # Init ROS Node
    rospy.init_node('Car_Control')
    # Init the moving status to False
    pub_cmd = False
    # Setup a new thread to run the while loop to wait and send signal
    T = threading.Thread(target=pub,args=[])
    # Chile thread will end with parent thread
    T.setDaemon(True)
    # Init publisher
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    # Init Speed array
    speed = [0, 0, 0, 0]
    # Start the child thread after all things are initialized
    T.start()
    print('------Program Begins------')
    # Main loop to get user input
    while True:
        IN = input('Command: ')
        if IN == '0':
            print('------Program Terminated------')
            break
        elif IN == '1':
            # Define a stop command
            # Stop sending commands
            pub_cmd = False
            # Reset all prarmeters
            for i in range(3):
                speed[i] = 0
            print()
        elif IN == '2':
            # Default moving mode speed 0.154 forward 1s
            parameters =  [0.154, 0, 0, 0]
            for i in range(3):
                speed[i] = parameters[i]
            pub_cmd = True
            time.sleep(1)
            pub_cmd = False
        else:
            continue


