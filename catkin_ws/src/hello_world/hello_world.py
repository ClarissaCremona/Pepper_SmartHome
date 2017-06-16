#!/usr/bin/python
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", 172.20.10.8, 9559)
tts.say("Hi there")
