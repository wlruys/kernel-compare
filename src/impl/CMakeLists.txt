set(BACKEND_SRC 
    impl.cpp
)

set(BACKEND_HDR
    impl.hpp
)

#Add "include" to all header files
foreach(HEADER ${BACKEND_HDR})
    set(BACKEND_HDR_INCLUDE ${BACKEND_HDR_INCLUDE} ${CMAKE_CURRENT_SOURCE_DIR}/${HEADER})
endforeach()

message(STATUS "ALL FILES: ${BACKEND_SRC}")

add_library(backend STATIC ${BACKEND_SRC})

set_target_properties(backend PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(backend PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(backend PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
set_target_properties(backend PROPERTIES PUBLIC_HEADER "${BACKEND_HDR_INCLUDE}")

install(TARGETS backend
    EXPORT ModuleBackendTargets
    LIBRARY DESTINATION .
)
