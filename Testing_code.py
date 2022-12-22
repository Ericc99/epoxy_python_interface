#!/usr/bin/env python3

import termios, sys
import rospy
import threading
from geometry_msgs.msg import Twist

class PublishThread(threading.Thread):
    # Initialize the Publish Thread
    def __init__(self):
        super(PublishThread, self).__init__()
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.th = 0.0
        self.speed = 0.0
        self.turn = 0.0
        self.condition = threading.Condition()
        self.done = False
        self.timeout = 0.02

        # Threading internal command to start the threading operation
        self.start()

    # Update the system operating condition
    def update(self, x, y, z, th, speed, turn):
        self.condition.acquire()
        self.x = x
        self.y = y
        self.z = z
        self.th = th
        self.speed = speed
        self.turn = turn




def Moving(pub):
    twist = Twist()
    twist.linear.x = 1
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    pub.publish(twist)



msg = """
What would you like to do?
    Type 0 to exit
    Type 1 to move 1m forward

"""

terminate = """
------ End of program ------
"""

if __name__ == '__main__':
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('Testing_Node')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    while True:
        IN = input(msg)
        if IN == '1':
            Moving(pub)
        elif IN == '0':
            break
        else:
            print('Unkown command.')
            continue
    print(terminate)




