#!/usr/bin/env python
# Title : teleop.py
# Author : Clarissa Cremona
# Date : 09/06/2017
# Version : 1.0

import roslib
import rospy

import sys, select, termios, tty

names  = ["HeadYaw", "HeadPitch"]
angles  = [0.0, 0.0]
fractionMaxSpeed  = 0.05
x = 0.2

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def move(key):
    global x
    if (key == '\x30'): # key '0' move forward
        motionProxy.post.moveTo(0.1, 0.0, 0.0)
    elif (key == '\x39'): # key '9' move backward
        motionProxy.post.moveTo(-0.1, 0.0, 0.0)
    elif (key == '\x32'): # key '1' turn right
        motionProxy.post.moveTo(0.0, 0.0, 0.25)
    elif (key == '\x31'): # key '2' turn left
        motionProxy.post.moveTo(0.0, 0.0, -0.25)
    elif (key == '\x33'): # key '3' turn head left
        if (x<1.04):
            x += 0.15
        angles = [x, -0.2]
        motionProxy.setAngles(names, angles, fractionMaxSpeed)
    elif (key == '\x34'): # key '4' turn head right
        if (x>-1.04):
            x -= 0.15
        angles = [x, -0.2]
        motionProxy.setAngles(names, angles, fractionMaxSpeed)

#def move_head(key):
#    if (key == '\x30'):

if __name__=="__main__":
    from naoqi import ALProxy
    motionProxy = ALProxy("ALMotion", "pepper.local", 9559)
    motionProxy.setStiffnesses("Head", 1.0)
    #motionProxy.rest()
    #motionProxy.wakeUp()
    #motionProxy.moveTo(0.0, 0.2, 0.0)
    settings = termios.tcgetattr(sys.stdin)
    while(1):
        key = getKey()
        if (key == '\x03'):
		          break
        print(key)
        move(key)
