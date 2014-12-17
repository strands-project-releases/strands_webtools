^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package strands_webtools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.2 (2014-11-05)
------------------
* merged `#62 <https://github.com/strands-project/strands_webtools/issues/62>`_
* Merge pull request `#60 <https://github.com/strands-project/strands_webtools/issues/60>`_ from cdondrup/hydro-devel
  strands_pedestrian_tracking has been renamed to mdl_people_tracker
* strands_pedestrian_tracking has been renamed to mdl_people_tracker
* Contributors: Christian Dondrup, Marc Hanheide

0.0.1 (2014-08-27)
------------------
* moved webserver.sh
* Merge pull request `#59 <https://github.com/strands-project/strands_webtools/issues/59>`_ from ToMadoRe/hydro-devel
  Fixed missing build dependencies
* Fixed missing build dependencies
* Merge pull request `#57 <https://github.com/strands-project/strands_webtools/issues/57>`_ from kunzel/master
  added chatbot and updated visualization of stats
* updated stats visualization
* Merge branch 'master' of https://github.com/strands-project/strands_webtools
* added link to bob s chatbot
* Merge pull request `#56 <https://github.com/strands-project/strands_webtools/issues/56>`_ from kunzel/master
  added Bob's current tour info as it is also reported by Linda
* Merge branch 'master' of https://github.com/strands-project/strands_webtools
* added Bob s current tour info as also reported by Linda
* Merge pull request `#55 <https://github.com/strands-project/strands_webtools/issues/55>`_ from kunzel/master
  added a dynamic robot map based on the google maps api and a current status of topics (without using websockets)
* Merge branch 'master' of https://github.com/strands-project/strands_webtools
* added dynamic robot map and current status
* Merge pull request `#54 <https://github.com/strands-project/strands_webtools/issues/54>`_ from kunzel/master
  Updated latest version of Bob's homepage
* fixed conflict in bob.html
* added latest changes to bob s home page
* fixed line break
* fixed typo
* added static map for bham env
* fixed problem with video stream
* Merge branch 'master' of https://github.com/strands-project/strands_webtools
* removed unused parts; included twitter accounts
* Merge pull request `#52 <https://github.com/strands-project/strands_webtools/issues/52>`_ from kunzel/master
  Website for Bob
* added initial html page for bob
* cahnged submodule
* added command for loading apache modules
* Merge pull request `#50 <https://github.com/strands-project/strands_webtools/issues/50>`_ from strands-project/marathon
  Marathon: massive pull request with all the developments for the marathon
* Merge pull request `#49 <https://github.com/strands-project/strands_webtools/issues/49>`_ from marc-hanheide/marathon
  Marathon: making the marathon.html site configurable for different sites via CMake
* * added gitignore for generated html files
  * removed outdated files
  * added generation of html pages according to cmake settings
* Merge branch 'marathon' of github.com:strands-project/strands_webtools into marathon
* added mjpeg_server params
* Update README.md
* Merge branch 'marathon' of github.com:strands-project/strands_webtools into marathon
* Merge branch 'marathon' of github.com:marc-hanheide/strands_webtools into marathon
* included safe mjpeg_server and adjusted topic
* corrected typo
* Merge pull request `#48 <https://github.com/strands-project/strands_webtools/issues/48>`_ from marc-hanheide/marathon
  Marathon as currently testing on http://lcas.lincoln.ac.uk/linda/marathon.html
* Update README.md
* Update README.md
* Merge branch 'marathon' of github.com:strands-project/strands_webtools into marathon
* now works at UOL
* Merge pull request `#46 <https://github.com/strands-project/strands_webtools/issues/46>`_ from marc-hanheide/marathon
  new file to launch the throttles on the robot for web publishing
* new file to launch the throttles on the robot for web publishing
* submodule
* Merge pull request `#44 <https://github.com/strands-project/strands_webtools/issues/44>`_ from marc-hanheide/marathon
  merge of most recent master changes into this branch
* Merge branch 'master' of github.com:strands-project/strands_webtools into marathon
* Merge pull request `#41 <https://github.com/strands-project/strands_webtools/issues/41>`_ from kunzel/master
  Swapped nav2djs submodule from kunzel/nav2djs to WPI-RAIL/nav2djs
* Merge pull request `#43 <https://github.com/strands-project/strands_webtools/issues/43>`_ from marc-hanheide/marathon
  removed robot_pose_publishers. fixes `#42 <https://github.com/strands-project/strands_webtools/issues/42>`_
* removed robot_pose_publishers. fixes `#42 <https://github.com/strands-project/strands_webtools/issues/42>`_
* added submodule WPI-RAIL/nav2djs
* deleted submodule kunzel/nav2djs
* Merge pull request `#40 <https://github.com/strands-project/strands_webtools/issues/40>`_ from marc-hanheide/marathon
  Marathon branch with safe rosbridge
* added marathon in index.html
* fixed path
* moved all apache specific files into the subdir as copies of the original ones with updates URIs
* reverted back to stand alone behaviour
* restructured to make it mergaeable with the master
* moved launch files
* Merge pull request `#39 <https://github.com/strands-project/strands_webtools/issues/39>`_ from marc-hanheide/apache_proxy
  I merge this myself, as it's only renaming things to work properly and only in this branch
* made it use the new rosbridge
* renamed and made it using the new rosbridge
* Merge pull request `#38 <https://github.com/strands-project/strands_webtools/issues/38>`_ from marc-hanheide/apache_proxy
  Apache proxy + new read-only version of rosbridge being used
* added mileage
* moved to linda/ namespace
* added RO version of webtools
* Update README.md
* Merge pull request `#37 <https://github.com/strands-project/strands_webtools/issues/37>`_ from marc-hanheide/apache_proxy
  some fixes to now work with the latest strands_morse
* * added meta tag to stop browsers caching these pages
  * change to the mono camera
  * fixed the topics correctly
* Merge branch 'apache_proxy' of github.com:strands-project/strands_webtools into apache_proxy
* changed image topic to match head_xtion
* Merge pull request `#36 <https://github.com/strands-project/strands_webtools/issues/36>`_ from marc-hanheide/apache_proxy
  new webtools setup using Apache. Closes `#34 <https://github.com/strands-project/strands_webtools/issues/34>`_
* added link to the original instructions
* Merge branch 'apache_proxy' of github.com:marc-hanheide/strands_webtools into apache_proxy
* disabled the simple webserver in the Apache setup
* simple script to build the wstunnel for Apache
* added the missing deps
* Update README.md
* completed instructions
* added instructions for installing apache modules
* stream-lined installation procedure with apache using cmake target "apache" and a new script
* now uses the proxied connection (all through port 80)
* change mjpeg port to not interfere with other services
* added mjpeg_server as dependency
* added missing css images
* fixed link
* added links
* Added info where to find topic_republisher (strands_utils)
* strands_utils -> topic_republisher
* Merge pull request `#32 <https://github.com/strands-project/strands_webtools/issues/32>`_ from kunzel/refactor-repo-structure
  Refactoring of repository structure
* added nav2djs submodule, adapted navigation.html
* included javascript files from submodules, removed obsolete javascript files
* added submodule for keyboardteleob
* added submodules for roslibjs, ros3djs, ros2djs and mjpegcanvasjs
* authors, license, changelog
* Merge pull request `#30 <https://github.com/strands-project/strands_webtools/issues/30>`_ from kunzel/nav-orientation
  Solves Issue `#29 <https://github.com/strands-project/strands_webtools/issues/29>`_
* Merge branch 'master' of https://github.com/strands-project/strands_webtools into nav-orientation
* centered map view by default, updated click instruction
* Merge pull request `#28 <https://github.com/strands-project/strands_webtools/issues/28>`_ from kunzel/nav-orientation
  2D navigation with orientation
* fixed typo
* Merge branch 'master' of https://github.com/strands-project/strands_webtools into nav-orientation
* 2d map navigation with orientation
* removed weird character
* added additional dependencies
* Merge pull request `#26 <https://github.com/strands-project/strands_webtools/issues/26>`_ from hawesie/master
  Added keyboard controls to move 2D nav map around in the viewer.
* Merge remote-tracking branch 'upstream/master'
* Added scrolling of 2D map view.
* Merge pull request `#25 <https://github.com/strands-project/strands_webtools/issues/25>`_ from hawesie/master
  Added tf2_web_republisher to launch and added robot pose visualisation to main view
* Merge remote-tracking branch 'upstream/master'
* Added tf2_web_republisher to launch file to ensure link between web tf and real tf. This fixed the tf problem with the visualisation and closes `#10 <https://github.com/strands-project/strands_webtools/issues/10>`_.
* Merge pull request `#23 <https://github.com/strands-project/strands_webtools/issues/23>`_ from hawesie/master
  Use robot_pose_publisher instead of the republisher I wrote. Also made this a valid catkin package.
* Made this a valid catkin package.
* Removed need for our own republisher.
  Instead relying on robot_pose_publisher which was designed to do this explicitly. See: https://github.com/WPI-RAIL/nav2djs/issues/26#issuecomment-20123090
* fixed typo
* Merge remote-tracking branch 'upstream/master'
* Merge pull request `#22 <https://github.com/strands-project/strands_webtools/issues/22>`_ from marc-hanheide/master
  now works also with remote access (not only localhost).
* Merge branch 'master' of github.com:strands-project/strands_webtools
* now works also with remote access (not only localhost).
* Merge pull request `#19 <https://github.com/strands-project/strands_webtools/issues/19>`_ from marc-hanheide/master
  added the republish_robot_pose node to the webtools launch file to get the entire webtools up and running at once
* Merge pull request `#21 <https://github.com/strands-project/strands_webtools/issues/21>`_ from kunzel/master
  added comment about the PTU joint state republisher
* added comment about the PTU joint state republisher
* added the https://github.com/marc-hanheide/strands_utils/blob/master/src/scripts/republish_robot_pose.py to the launch file
* Merge pull request `#18 <https://github.com/strands-project/strands_webtools/issues/18>`_ from kunzel/ptu-msg
  changed ptu msg from Vector3 (morse) to JointState (real robot)
* changed ptu msg from Vector3 (morse) to JointState (real robot)
* Merge pull request `#17 <https://github.com/strands-project/strands_webtools/issues/17>`_ from hawesie/master
  Added nodes on robot_pose for 2D nav view
* Merge remote-tracking branch 'upstream/master'
* Added comments on how to deal with robot pose. Fixes `#12 <https://github.com/strands-project/strands_webtools/issues/12>`_.
* Merge pull request `#15 <https://github.com/strands-project/strands_webtools/issues/15>`_ from kunzel/ptu
  added teleop control for PTU
* added teleop control for PTU
* Cleaned up formatting errors for .rosinstall text.
* Removed unnecessary map file.
* Merge pull request `#11 <https://github.com/strands-project/strands_webtools/issues/11>`_ from marc-hanheide/master
  Initial version of a simple navigation widget to send the robot around in the 2D map
* added 2D navigation widget for autonomous navigation in the map
* added *~ to gitignore
* Merge pull request `#8 <https://github.com/strands-project/strands_webtools/issues/8>`_ from kunzel/master
  added 3d map and pose to main view
* Update README.md
* added pose to main view
* Merge branch 'master' of https://github.com/strands-project/strands_webtools
* added 3D map to main view
* Merge pull request `#7 <https://github.com/strands-project/strands_webtools/issues/7>`_ from marc-hanheide/master
  Launch file for webtools in strands
* added launch file. fixes `#4 <https://github.com/strands-project/strands_webtools/issues/4>`_. also added a simple static index.html
* Merge pull request `#3 <https://github.com/strands-project/strands_webtools/issues/3>`_ from hawesie/master
  Added additional page plus updated read me
* Added run instructions.
* Refactored a little and added map page.
  Map page may not be necessary if we include on page with camera as discussed.
* added more dependencies to README
* Merge pull request `#2 <https://github.com/strands-project/strands_webtools/issues/2>`_ from kunzel/master
  added keyboard control and robot cam view
* added keyboard control and robot cam view
* Merge pull request `#1 <https://github.com/strands-project/strands_webtools/issues/1>`_ from hawesie/master
  Links in README
* adding some links for marc
* Initial commit
* Contributors: Lars Kunze, Marc Hanheide, Nick Hawes, Webuser, thomas.faeulhammer@tuwien.ac.at
