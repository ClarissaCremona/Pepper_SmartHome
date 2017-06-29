#!/usr/bin/env python
# Title : iot_test.py
# Author : Clarissa Cremona
# Date : 09/06/2017
# Version : 1.0

import rospy
#from std_msgs.msg import String
from diagnostic_msgs.msg import KeyValue # this is the message type /iot_updates uses

def callback(data):
    print(data.key + " " + data.value)
    if(data.key == "Light_GF" and data.value == "ON"):
        #tts.say("The light is on")
        #animatedProxy.say("^startTag(body language) \\vct=100\\Your friend has put the kettle on. Would you like to join them for a cup of tea?^stopTag(body language)")
        postureProxy.goToPosture("StandInit", 0.5)
        print("The light is on!")
    elif(data.key == "Light_GF" and data.value == "OFF"):
        #tts.say("The light is off")
        animatedProxy.say("^startTag(body language) The light is off.")
        print("The light is off")
        postureProxy.goToPosture("StandInit", 0.5)
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s %s', data.key, data.value)

def listener():
    rospy.init_node('pepper_listener', anonymous=True) # create node to subscribe to topic
    rospy.Subscriber("iot_updates", KeyValue, callback) # subscribe to topic /iot_updates
    rospy.spin() # keeps python from exiting until node is stopped
    #print(data.value)

if __name__ == '__main__':
    from naoqi import ALProxy
    tts = ALProxy("ALTextToSpeech", "pepper.local", 9559)
    animatedProxy = ALProxy("ALAnimatedSpeech", "pepper.local", 9559)
    postureProxy = ALProxy("ALRobotPosture", "pepper.local", 9559)
    tts.setParameter("speed", 90)
    listener()
