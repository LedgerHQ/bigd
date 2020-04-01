add_library(bigd
    ${CMAKE_CURRENT_SOURCE_DIR}/bigd.c
    ${CMAKE_CURRENT_SOURCE_DIR}/bigdigits.c
)

target_include_directories(bigd
    PRIVATE 
        ${CMAKE_CURRENT_SOURCE_DIR}
    SYSTEM PUBLIC
        $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)

