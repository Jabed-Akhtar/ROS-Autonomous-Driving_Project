#!/usr/bin/env python2

# importing packages
import os
import sys
#import cv2
import time

# importing ros packages
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

#sensor_msgs/LaserScan

def callback(msg):
    angle_min =  msg.angle_min
    angle_max = msg.angle_max
    rospy.loginfo('angle_min: {}, angle_max: {}'.format(angle_min, angle_max))

def main():
    rospy.init_node('vehicle_auto')
    #rospy.Subscriber("/car_autonom/laser/scan", LaserScan, callback)
    #rospy.spin()
    pub = rospy.Publisher('chatter', String, queue_size=10)
    #rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    hello_str = "hello world %s" % rospy.get_time()
    rospy.loginfo(hello_str)
    pub.publish(hello_str)


if __name__ == '__main__':
    main()

# ----------------------------- END OF FILE --------------------------
