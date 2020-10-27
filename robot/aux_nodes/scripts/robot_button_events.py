#!/usr/bin/env python

import roslib
import rospy
from aux_nodes.msg import ButtonEvent
import json

class ButtonState():

	def __init__(self, namespace = ''):
		self.ns = namespace
		self.buttonID = ""
		self.buttonstate = None

		rospy.init_node(str(self.ns + "/button_event"))		
		rospy.Subscriber(str(self.ns + "/events/button"),ButtonEvent,self.ButtonEventCallback)
		rospy.spin();

	def ButtonEventCallback(self,data):
		self.buttonID = data.button
		self.buttonstate = data.state
	
	def run(self):
		data = {
			"ButtonID" : self.buttonID,
			"ButtonState" : self.buttonstate
		}

		return json.dump(data)

if __name__ == '__main__':
	try:
		ButtonState()
	except rospy.ROSInterruptException:
		rospy.loginfo("exception")
