cmake_minimum_required(VERSION 2.8.3)
project(strands_webtools)
 

add_custom_target(apache)

add_custom_command(TARGET apache
	WORKING_DIRECTORY ${strands_webtools_SOURCE_DIR}/apache
	COMMAND bash -x ./configure_apache.sh
)

add_subdirectory (apache)

 
## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS robot_pose_publisher rosbridge_library rosbridge_server)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/groovy/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES strands_webtools
#  CATKIN_DEPENDS robot_pose_publisher rosbridge_suite
#  DEPENDS system_lib
)


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/groovy/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS
  scripts/webserver.sh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark executables and/or libraries for installation
# install(TARGETS strands_webtools strands_webtools_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )


install(DIRECTORY roslibjs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/roslibjs
)

install(DIRECTORY ros3djs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/ros3djs
)
install(DIRECTORY ros2djs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/ros2djs
)
install(DIRECTORY nav2djs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/nav2djs
)
install(DIRECTORY mjpegcanvasjs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/mjpegcanvasjs
)
install(DIRECTORY keyboardteleopjs/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/keyboardteleopjs
)

install(DIRECTORY js/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/js
)
install(DIRECTORY css/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/css
)


install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)




## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_strands_webtools.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
