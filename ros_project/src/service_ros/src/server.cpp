#include <ros/ros.h>
#include <service_ros/greeting.h>
#include <string.h>

bool function(service_ros::greeting::Request& req,service_ros::greeting::Response& res)
{
 ROS_INFO("Request from %s with age %d",req.name.c_str(),req.age);
 res.feedback="Hi "+req.name+". I'm server!";
 return true;
}

int main(int argc, char **argv)
{
 ros::init(argc,argv,"server_node"); 
 ros::NodeHandle nh;
 service_ros::greeting srv;
 ros::ServiceServer service=nh.advertiseService("greeting",function);
 ros::spin();
 return 0;
}
