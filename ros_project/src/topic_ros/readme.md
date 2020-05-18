## 编译修改
1. CMakeLists.txt 
 -[x] add_message_files(FILES gps.msg)
 -[x] generate_messages(DEPENDENCIES std_msgs)
 -[x] catkin_package(CATKIN_DEPENDS message_runtime roscpp rospy std_msgs)
 -[x] add_executable(talker_node src/talker.cpp)(listener同理)
 -[x] add_dependencies(talker_node topic_ros_generate_messages_cpp)(listner同理)
 -[x] target_link_libraries(talker_node ${catkin_LIBRARIES})(listen同理)
2. package.xml
只添加了：<exec_depend>message_runtime</exec_depend>

## topic通信的主构建流程
1. 新建msg/gps.msg，定义数据格式
2. 构建后添加CMakeLists.txt中的msg路径及报生成依赖就可编译生成gps.h的头文件
3. 添加c艹版的talker.cpp和listener.cpp(/src)
4. 添加python版的talker.py和listener.py(/scripts)
5. 编译运行

### 主程序编写流程（cpp与py语法稍有不同，这里以cpp为例）
1. talker.cpp
 -[x] 包含头文件ros/ros.h topic_ros/gps.h
 -[x] node初始化 ros::init(argc,argv,"talker_node")
 -[x] 定义操作指针ros::NodeHandle nh，消息实例ros::gps msg
 -[x] 定义发布消息 ros::Publisher pub=nh.advertise<topic_ros::gps>("gps_info",1)
 -[x] 定义发布循环的间隔 ros::Rate loop_rate(1.0)
 -[x] 循环判断 while(ros::ok())
 -[x] 发布消息 pub publish(msg)
 -[x] 延时 loop_rate.sleep()
2. listener.cpp
 -[x] 同上
 -[x] 同上
 -[x] 同上
 -[x] 定义回调函数 callback(const ros::topic_ros::gps::constPtr& msg)
 -[x] 对消息的内容进行自定义处理，可调用显示函数 ROS_INFO(...)
 -[X] 主函数流程：ros::Subscriber sub=subscribe("gps_info",1,callback)
 -[x] 等待函数调用 ros::spin()
