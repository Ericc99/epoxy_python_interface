import threading
import time
import rospy
from geometry_msgs.msg import Twist

def pub():
    while True:
        if pub_cmd == 0:
            pass
        else:
            print('Publishing data: GG')
            move()
            time.sleep(0.2)

def move():
    twist = Twist()
    twist.linear.x = 0.3
    twist.linear.y = 0
    twist.linear.z = 0
    twist.angular.x = 0
    twist.angular.y = 0
    twist.angular.z = 0

    publisher.publish(twist)


def timer(duration):
    time.sleep(duration)
    return  

if __name__ == '__main__':
    rospy.init_node('Testing_Node')
    global pub_cmd
    pub_cmd = 0
    T = threading.Thread(target = pub, args=[])
    T.setDaemon(True)
    T.start()
    global publisher
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    while True:
        IN = input('Command:')
        if IN == '0':
            print('Threads TERMINATED')
            break
        elif IN == '1':
            if T.is_alive() and pub_cmd == 1:
                print('T is now DEAD')
                pub_cmd = 0
                
            elif T.is_alive() and pub_cmd == 0:
                print('T is now RUNNING')
                pub_cmd = 1
        elif IN == '2':
            duration = input('Running time:')
            print('T is STARTED')
            pub_cmd = 1
            timer(int(duration))
            pub_cmd = 0
            print('T STOPPED after ' + str(duration) + 's')
        else:
            continue
    
