#include <ros/ros.h>
#include <service_ros/greeting.h>

int main(int argc, char **argv)
{
 ros::init(argc,argv,"client_node");
 ros::NodeHandle nh;
 service_ros::greeting srv;
 ros::ServiceClient client=nh.serviceClient<service_ros::greeting>("greeting");
 srv.request.name="HAN";
 srv.request.age=20;
 if (client.call(srv))
{
 ROS_INFO("Response from server: %s",srv.response.feedback.c_str());
}
 else
{
 ROS_ERROR("Failed to call service Service_demo");
 return 1;
}
 return 0;
}
