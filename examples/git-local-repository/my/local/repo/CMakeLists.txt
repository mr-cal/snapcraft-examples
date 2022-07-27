cmake_minimum_required(VERSION 2.6)

project(hello-world CXX)

add_executable(hello-world src/hello-world.cpp)

install(TARGETS hello-world RUNTIME DESTINATION bin)
