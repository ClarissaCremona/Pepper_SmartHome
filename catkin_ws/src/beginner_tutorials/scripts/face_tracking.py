#!/usr/bin/env python
# Title : teleop.py
# Author : Clarissa Cremona
# Date : 09/06/2017
# Version : 1.0

import rospy
import sys

USAGE = "USAGE:\n" \
        "python vision_setfacetracking.py [NAO_IP] [0 or 1] \n" \
        "\nExamples: \n" \
        "Enable tracking: face_tracking.py 192.168.1.8 1\n" \
        "Disable tracking: face_tracking.py 192.168.1.8 0"

from naoqi import ALProxy

def set_pepper_face_detection_tracking(pepper_ip, pepper_port, tracking_enabled):
    # Create a proxy to nao's ALFaceDetection and enable/disable tracking.
    faceProxy = ALProxy("ALFaceDetection", pepper_ip, pepper_port)

    print "Will set tracking to '%s' on the robot ..." % tracking_enabled

    # Enable or disable tracking.
    faceProxy.enableTracking(tracking_enabled)

    # Just to make sure correct option is set.
    print "Is tracking now enabled on the robot?", faceProxy.isTrackingEnabled()

def main():
    # Specify your IP address here.
    pepper_ip = "192.168.1.8"
    pepper_port = 9559

    tracking_enabled = True

    try:
        if len(sys.argv) > 1:
            pepper_ip = sys.argv[1]

        if len(sys.argv) > 2:
            tracking_enabled = bool(int(sys.argv[2]))

        set_pepper_face_detection_tracking(pepper_ip, pepper_port, tracking_enabled)

    except Exception as e:
        print "Exception Caught: %s\n" % e
        print USAGE

if __name__ == '__main__':
    main()
