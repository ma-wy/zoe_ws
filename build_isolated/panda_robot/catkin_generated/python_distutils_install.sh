#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/abml/zoe_ws/src/Franka/panda_robot"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/abml/zoe_ws/install_isolated/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/abml/zoe_ws/install_isolated/lib/python3/dist-packages:/home/abml/zoe_ws/build_isolated/panda_robot/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/abml/zoe_ws/build_isolated/panda_robot" \
    "/usr/bin/python3" \
    "/home/abml/zoe_ws/src/Franka/panda_robot/setup.py" \
    egg_info --egg-base /home/abml/zoe_ws/build_isolated/panda_robot \
    build --build-base "/home/abml/zoe_ws/build_isolated/panda_robot" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/abml/zoe_ws/install_isolated" --install-scripts="/home/abml/zoe_ws/install_isolated/bin"
