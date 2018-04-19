# Script generated with Bloom
pkgdesc="ROS - This package provides a script that launches Emacs with Slime (the Superior Lisp Interaction Mode) ready for Lisp development and roslisp."


pkgname='ros-kinetic-roslisp-repl'
pkgver='0.4.12_1'
pkgrel=1
arch=('any')
license=('Public domain'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-rosemacs'
'ros-kinetic-roslisp'
'ros-kinetic-slime-ros'
'ros-kinetic-slime-wrapper'
'sbcl'
)

conflicts=()
replaces=()

_dir=roslisp_repl
source=()
md5sums=()

prepare() {
    cp -R $startdir/roslisp_repl $srcdir/roslisp_repl
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

