#!/usr/bin/env python
# Title : camera_view.py
# Author : Clarissa Cremona
# Date : 09/06/2017
# Version : 1.0

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I can see %s', data.data)

def read_camera():
    rospy.init_node('iot_view', anonymous=True)
    rospy.Subscriber('/iot_updates', String, callback)

if __name__ == '__main__':
    read_camera()
    rospy.spin()
