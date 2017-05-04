Name:           ros-jade-slime-wrapper
Version:        0.4.11
Release:        0%{?dist}
Summary:        ROS slime_wrapper package

Group:          Development/Libraries
License:        Public domain
URL:            http://common-lisp.net/project/slime
Source0:        %{name}-%{version}.tar.gz

Requires:       emacs
BuildRequires:  ros-jade-catkin

%description
ROS wrapper for slime

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu May 04 2017 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.11-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.10-0
- Autogenerated by Bloom

* Tue Dec 22 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.9-0
- Autogenerated by Bloom

* Wed Sep 16 2015 Gayane Kazhoyan <kazhoyan@cs.uni-bremen.de> - 0.4.8-0
- Autogenerated by Bloom

