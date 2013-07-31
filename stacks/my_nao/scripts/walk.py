#!/usr/bin/env python

import roslib
roslib.load_manifest('nao_driver')
import rospy

from nao_driver import *

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose2D
from sensor_msgs.msg import JointState
from std_msgs.msg import Bool
import std_msgs.msg

import nao_msgs.srv

import cv

def walker():
	c = rospy.Publisher('cmd_vel', Twist)
	rospy.init_node('walking_TEST')
	s = rospy.Publisher('speech', String)
	s.publish("I am going to walk now.")
	for i in range(30):
		twist = Twist()
		twist.linear.x = 1.0
		c.publish(twist)
		rospy.sleep(0.1)
	twist = Twist()
	c.publish(twist)
	s.publish("Stopping")

if __name__ == '__main__':
	try:
		walker()
	except rospy.ROSInterruptException:
		pass