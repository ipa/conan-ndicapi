PROJECT(OpenIGTLinkTest)

cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

ADD_EXECUTABLE(ndicapitest   main.cpp)
TARGET_LINK_LIBRARIES(ndicapitest CONAN_PKG::NDICAPI)
#message(${CONAN_INCLUDE_DIRS_OPENIGTLINK})
