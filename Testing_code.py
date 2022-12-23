#!/usr/bin/env python3

import termios, sys
import rospy
import threading
from geometry_msgs.msg import Twist

def Moving(pub):
    twist = Twist()
    twist.linear.x = 0.1
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




