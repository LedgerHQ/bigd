cmake_minimum_required(VERSION 2.8.12)
project(bigd-test-pkg C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(bigd-test-pkg main.c)
target_link_libraries(bigd-test-pkg ${CONAN_LIBS})