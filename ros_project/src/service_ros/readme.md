## cpp操作流程
1. rosrun service_ros server_node 发布server_node节点，构建服务消息类型greeting，等待client服务消息修改，使用ROS_INFO显示Request from server（消息修改内容），定义res.feedback内容。
2. rosrun service_ros client_node 发布client_node节点,确定服务消息类型greeting，对服务消息进行赋值，返回给server_node节点，并使用ROS_INFO显示Response from server,显示res.feedback对应srv.response.feedback存储的值。
3. server_node采用函数调用方式，定义请求响应指针
`service_ros::greeting::Request& req,service_ros::greeting::Response& res`,client_node使用`client.call(srv)`返回值判断通信是否建立。


## py操作流程
1. python server.py 从client.py req获取name,age实例对象，调用`srvResponse`返回req.name
2. python client.py 调用`rep=client.call()`写入实例，调用%rep.feedback返回消息到server.py
