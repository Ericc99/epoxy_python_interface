import rospy
from sensor_msgs.msg import Imu

def doData(imu):
    rospy.loginfo(imu.header)


if __name__ == '__main__':
    rospy.init_node('Test_Listen')

    sub = rospy.Subscriber('/imu', Imu, doData, queue_size=1000)

    rospy.spin()