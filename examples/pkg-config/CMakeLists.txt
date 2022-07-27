cmake_minimum_required(VERSION 2.6)
project(hello-world CXX)

include(FindPkgConfig)

pkg_check_modules(MIRAL miral REQUIRED)

add_executable(hello-world src/hello-world.cpp)

target_include_directories(hello-world PUBLIC SYSTEM ${MIRAL_INCLUDE_DIRS})
target_link_libraries(hello-world ${MIRAL_LDFLAGS})

install(TARGETS hello-world RUNTIME DESTINATION bin)
