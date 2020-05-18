#!/usr/bin/env python
# coding utf-8
import rospy
from service_ros.srv import *
def callback():
    rospy.init_node('client_node')
    rospy.wait_for_service("greeting")
    try:
        client=rospy.ServiceProxy("greeting",greeting)
 	rep=client.call("HAN",20)
   	rospy.loginfo("Message From server:%s" %rep.feedback)
    except rospy.ServiceException,e:
	rospy.logwarn("Service call failed: %s" %e)

if __name__ == "__main__":
    callback()
