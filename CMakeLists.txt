cmake_minimum_required(VERSION 2.8.3)
project(JGame)

find_package(catkin_simple REQUIRED)
catkin_simple(ALL_DEPS_REQUIRED)

catkin_package()


cs_install()
cs_export()
