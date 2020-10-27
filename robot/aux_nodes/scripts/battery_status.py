#!/usr/bin/env python
import roslib
import rospy
from sensor_msgs.msg import BatteryState
import json


class Battery():

	def __init__(self, namespace = ""):
		'''
		sensor_msgs.BatteryState.msg
		Returns information about battery status of the robot including
		- Battery percentage
		- Battery charge
		- Battery Current

		Returns in the form of JSON
		'''

		rospy.init_node( str(namespace+"Battery-Status"))

		rospy.Subscriber("/battery_charge/",BatteryState,self.PowerEventCallback)

		#rospy.spin() tells the program to not exit until you press ctrl + c.  If this wasn't there... it'd subscribe to /laptop_charge/ then immediatly exit (therefore stop "listening" to the thread).
		rospy.spin();

	def PowerEventCallback(self,data):
		print("Percentage: "+ str(data.percentage))
		print("Charge: " + str(data.charge)) 
		print("Current: " + str(data.current))
		print("Battery is present: "+ str(data.battery))

		if(int(data.charge_state) == 1):
			print("Currently charging")
		else:
			print("Not charging")
		print("-----")
		#Tip: try print(data) for a complete list of information available in the /laptop_charge/ thread

	def exportJSON(self):
		data = {
			'isBattery' : self.isBattery,
			'percentage' : self.percentage,
			'charge': self.charge,
			'current' : self.current}

		return json.dump(data)
	
if __name__ == '__main__':
	try:
		Battery()
	except rospy.ROSInterruptException:
		rospy.loginfo("exception")
