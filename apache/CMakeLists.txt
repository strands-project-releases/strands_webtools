cmake_minimum_required(VERSION 2.8.3)
project(strands_webtools)

set(ROSWS "/linda/rosws" CACHE STRING "the suffix for the reverse proxy to the ROS bridge")
set(WT_POSE "/webthrottle/amcl_pose" CACHE STRING "the topic of the throttled pose")
set(WT_MILEAGE "/webthrottle/mileage" CACHE STRING "the topic of the throttled mileage")
set(MJPEG_URL "80/linda/video" CACHE STRING "the suffix for the web_video_server accessed via reverse proxy")
set(WT_MJPEG_TOPIC "/image_blurrer/output_video" CACHE STRING "the topic of the image stream for the web_video_server")
set(LOGO_URL "http://www.lincoln.ac.uk/home/media/universityoflincoln/styleassets/images/logo-white.png" CACHE STRING "an URL to your institute's logo")

configure_file(marathon.html.in ${CMAKE_CURRENT_SOURCE_DIR}/marathon.html)

