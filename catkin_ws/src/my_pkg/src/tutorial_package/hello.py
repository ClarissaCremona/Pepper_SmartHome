#from naoqi import ALProxy
#tts = ALProxy("ALTextToSpeech", "192.168.1.8", 9559)
#tts.say("Congratulations!")
#print("Hello it worked")
'''
import time
import argparse
from naoqi import ALProxy
'''
'''
motionProxy = ALProxy("ALMotion", "pepper.local", 9559)
tts = ALProxy("ALTextToSpeech", "pepper.local", 9559)

motionProxy.setStiffnesses("Head", 1.0)

    # Example showing how to set angles, using a fraction of max speed
names  = ["HeadYaw", "HeadPitch"]
angles  = [0.2, -0.2]
fractionMaxSpeed  = 0.1
motionProxy.setAngles(names, angles, fractionMaxSpeed)

time.sleep(3.0)
motionProxy.setStiffnesses("Head", 0.0)

tts.say("I recommend you take those pills after lunch")
'''
import math
import time
def rest() :

	from naoqi import ALProxy
	tts = ALProxy("ALTextToSpeech", "192.168.1.8", 9559)
	motionProxy = ALProxy("ALMotion", "pepper.local", 9559)
	postureProxy = ALProxy("ALRobotPosture", "pepper.local", 9559)
	navigationProxy = ALProxy("ALNavigation", "pepper.local", 9559)
	navigationProxy.post.moveAlong(["Composed", ["Holonomic", ["Line", [0.3, 0.0]], 0.0, 5.0], ["Holonomic", ["Line", [-0.3, 0.0]], 0.0, 6.0]])
	#while motionProxy.moveIsActive():
	#	tts.say("I'm walking here")
	#postureProxy.goToPosture("StandInit", 0.5)
	#motionProxy.moveTo(0.2, 0.0, 0.2)
	#motionProxy.wakeUp()
	#motionProxy.moveInit()
    	#motionProxy.moveTo(0.2, 0.0, 0.0)
'''
	names  = ["HeadYaw", "HeadPitch"]
	angles  = [-0.2, 0]
	fractionMaxSpeed  = 0.1
	#motionProxy.setAngles(names, angles, fractionMaxSpeed)
	time.sleep(1)
	#motionProxy.rest()
'''





'''
from naoqi import ALProxy
move = ALProxy("ALMotion", "192.168.1.8", 9559)
move.openHand('LHand')
move.closeHand('LHand')
move.openHand('RHand')
move.closeHand('RHand')
'''
'''
class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self, False)

    def onLoad(self):
        self.motion = ALProxy( "ALMotion" )
        self.bIsRunning = False

    def onUnload(self):
        self.bIsRunning = False

    def onInput_onStart(self):
        if( self.bIsRunning ):
            return
        self.bIsRunning = True
        try:
            hands = []
            if( self.getParameter("Side") in ["Left", "Both"] ):
                hands.append( "LHand" )
            if( self.getParameter("Side") in ["Right", "Both"] ):
                hands.append( "RHand" )
            ids = []
            for hand in hands:
                if( self.getParameter("Action") == "Open the hand" ):
                    ids.append( self.motion.post.openHand(hand) )
                else:
                    ids.append( self.motion.post.closeHand(hand) )
            for id in ids:
                self.motion.wait( id, 0 )
        finally:
            self.bIsRunning = False
            self.onDone() # activate output of the box
'''
