#!/usr/bin/env python
#coding=utf-8
import rospy
from topic_ros.msg import gps

def talker():
    pub=rospy.Publisher("gps_info",gps,queue_size=10)
    rospy.init_node('pytalker',anonymous=True)
    rate=rospy.Rate(1)
    x=1.0
    y=2.0
    state='working'
    while not rospy.is_shutdown():
	rospy.loginfo('talker:gps:x=%f,y=%f',x,y)
	pub.publish(gps(state,x,y))
	x=1.03*x
	y=1.01*y
	rate.sleep()
if __name__ =="__main__":
    talker()
