#!/usr/bin/env python
#coding utf-8
import rospy
from service_ros.srv import *

def callback():
    rospy.init_node("server_node")
    s=rospy.Service("greeting",greeting,handle_function)
    rospy.loginfo("Ready to handle the request:")
    rospy.spin()

def handle_function(req): 
    rospy.loginfo("Request from %s with age %d",req.name,req.age)   
    return greetingResponse("Hi %s. I' server!" %req.name)

if __name__ == "__main__":
    callback()
