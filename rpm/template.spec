Name:           ros-kinetic-socketcan-bridge
Version:        0.7.2
Release:        0%{?dist}
Summary:        ROS socketcan_bridge package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/socketcan_bridge
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-can-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-socketcan-interface
BuildRequires:  ros-kinetic-can-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-socketcan-interface

%description
Provides nodes to convert messages from SocketCAN to a ROS Topic and vice versa.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue Mar 28 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.2-0
- Autogenerated by Bloom

* Mon Mar 20 2017 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.1-0
- Autogenerated by Bloom

* Thu Dec 15 2016 Mathias Lüdtke <mathias.luedtke@ipa.fraunhofer.de> - 0.7.0-0
- Autogenerated by Bloom

