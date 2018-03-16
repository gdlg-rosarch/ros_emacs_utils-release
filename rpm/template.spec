Name:           ros-kinetic-ros-emacs-utils
Version:        0.4.12
Release:        0%{?dist}
Summary:        ROS ros_emacs_utils package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-rosemacs
Requires:       ros-kinetic-roslisp-repl
Requires:       ros-kinetic-slime-ros
Requires:       ros-kinetic-slime-wrapper
BuildRequires:  ros-kinetic-catkin

%description
A metapackage of Emacs utils for ROS. Only there for simplifying the release
process.

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
* Fri Mar 16 2018 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.12-0
- Autogenerated by Bloom

* Thu May 04 2017 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.11-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.10-0
- Autogenerated by Bloom

* Mon Jul 18 2016 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.9-0
- Autogenerated by Bloom

