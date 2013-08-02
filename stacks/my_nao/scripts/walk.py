#!/usr/bin/env python

import roslib
roslib.load_manifest('nao_driver')
import rospy

from nao_driver import *

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from sensor_msgs.msg import JointState, Image
from std_msgs.msg import Bool
import std_msgs.msg

import nao_msgs.srv
from nao_msgs.msg import JointAnglesWithSpeed
from nao_msgs.msg import FadeRGB

import sys
import cv
from cv_bridge import CvBridge, CvBridgeError

class Nao:

	def __init__(self):
		self.cmd_vel = rospy.Publisher('cmd_vel', Twist)
		self.speech = rospy.Publisher('speech', String)
		self.joints = rospy.Publisher('joint_angles', JointAnglesWithSpeed)

		rospy.init_node('my_nao_test')

		cv.NamedWindow("display", 1)
		self.bridge = CvBridge()
		#self.image_sub = rospy.Subscriber("nao_camera", Image, self.img_callback)

		t = FadeRGB()
		print t

		#self.walker()
		'''joints = JointAnglesWithSpeed()
		joints.joint_names.append("LHand")
		joints.joint_angles.append(0.0)
		joints.speed = 1.0
		self.joints.publish(joints)'''


	def walker(self):
		self.speech.publish("Walking")
		for i in range(30):
			twist = Twist()
			twist.linear.x = 1.0
			self.cmd_vel.publish(twist)
			rospy.sleep(0.1)
		twist = Twist()
		self.cmd_vel.publish(twist)
		self.speech.publish("Stopping")


	def img_callback(self,data):
		try:
			cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
		except CvBridgeError, e:
			print e

		(cols,rows) = cv.GetSize(cv_image)
		cv.Circle(cv_image, (50,50), 10, 255)

		cv.ShowImage("display", cv_image)
		cv.WaitKey(3)


if __name__ == '__main__':
	try:
		n = Nao()
		#rospy.spin()
	except rospy.ROSInterruptException:
		pass