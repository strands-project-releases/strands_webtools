Name:           ros-indigo-strands-webtools
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS strands_webtools package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-mjpeg-server
Requires:       ros-indigo-robot-pose-publisher
Requires:       ros-indigo-rosapi
Requires:       ros-indigo-rosauth
Requires:       ros-indigo-rosbridge-library
Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-scitos-description
Requires:       ros-indigo-tf2-web-republisher
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mjpeg-server
BuildRequires:  ros-indigo-robot-pose-publisher
BuildRequires:  ros-indigo-rosapi
BuildRequires:  ros-indigo-rosauth
BuildRequires:  ros-indigo-rosbridge-library
BuildRequires:  ros-indigo-rosbridge-server
BuildRequires:  ros-indigo-scitos-description
BuildRequires:  ros-indigo-tf2-web-republisher

%description
Remote control our robots via a browser

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Nov 02 2014 Lars Kunze <l.kunze@cs.bham.ac.uk> - 0.0.1-0
- Autogenerated by Bloom

