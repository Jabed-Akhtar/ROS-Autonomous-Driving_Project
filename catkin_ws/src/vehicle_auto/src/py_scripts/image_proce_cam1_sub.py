#!/usr/bin/env python

# importing packages
import os
import sys
import cv2 as cv
import time

# importing ros packages
import rospy
from sensor_msgs.msg import Image

#sensor_msgs/LaserScan

def callback(msg):
    hei = msg.height
    wid = msg.width
    encod = msg.encoding
    is_bigend = msg.is_bigendian
    stp = msg.step
    data = msg.data

    #img_shape = type(data.shape)

    #print(data)
    rospy.loginfo('height: {}, width: {}, data_shape: {}'.format(hei, wid, img_shape))

    # image processing ---------------------------------------------------------
    #dir_path = os.path.dirname(__file__)
    #cv.imwrite(os.path.join(dir_path, '../Datas/Images/cam1/pic.jpg'), data)

def main():
    rospy.init_node('car_autonom')
    rospy.Subscriber("/car_autonom/camera1/image_raw", Image, callback)

    rospy.spin()

if __name__ == '__main__':
    main()

# ----------------------------- END OF FILE --------------------------
