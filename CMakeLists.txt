cmake_minimum_required(VERSION 3.10)
project(bigd VERSION 2.6.1 LANGUAGES C)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

add_subdirectory(src)

# Create an alias for build tree usage
add_library(BIGD::bigd ALIAS bigd)

include(GNUInstallDirs)
set(INSTALL_DIR ${CMAKE_INSTALL_LIBDIR}/cmake/BIGD)

install(
    TARGETS bigd
    EXPORT bigd-targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# Export the targets to a script
install(
    EXPORT bigd-targets
    FILE BIGDTargets.cmake
    NAMESPACE BIGD::
    DESTINATION ${INSTALL_DIR}
)

# Create a version file
include(CMakePackageConfigHelpers)
write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/BIGDConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

configure_package_config_file(
    ${CMAKE_CURRENT_LIST_DIR}/cmake/BIGDConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/BIGDConfig.cmake
    INSTALL_DESTINATION ${INSTALL_DIR}
)

# Install the configuration files
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/BIGDConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/BIGDConfigVersion.cmake
    DESTINATION ${INSTALL_DIR}
)

# Export from the build tree
export(EXPORT bigd-targets
    FILE ${CMAKE_CURRENT_BINARY_DIR}/BIGDTargets.cmake
    NAMESPACE BIGD::)

# Register package in user's package registry
export(PACKAGE bigd)