#!usr/bin/env python
#coding=utf-8
import rospy
import math
from topic_ros.msg import gps

def callback(gps):
    distance=math.sqrt(math.pow(gps.x,2)+math.pow(gps.y,2))
    rospy.loginfo("listener:gps:distance:%f,state=%s",distance,gps.state)
def listener():
    rospy.init_node('pylistener',anonymous=True)
    rospy.Subscriber("gps_info",gps,callback)
    rospy.spin()
if __name__ == "__main__":
    listener()
