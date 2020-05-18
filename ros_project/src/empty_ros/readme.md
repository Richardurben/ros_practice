## 客户端创建
1. qtcreator（推荐）# 可创建catkin工作区，也可以构建ropkg，bug：构建文件需要重启后才能显示文件
2. roboware studio # 有显示的bug
3. vscode # 万金油

## 手动创建(完整的ros工程)
```
mkdir empty_ros
cd empty_ros
mkdir src
cd src
catkin_init_workspace
cd ..
catkin_make # 编译产生devel build文件夹
source devel/setup.sh # 手动注册bash
echo $ROS_PACKAGE_PATH # 验证
cd src
catkin_create_pkg empty_ros roscpp rospy message_generation std_msgs
cd .. 
catkin_make
```
