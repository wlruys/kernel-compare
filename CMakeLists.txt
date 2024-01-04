cmake_minimum_required(VERSION 3.14)
set(CMAKE_CXX_STANDARD 17)

project(${SKBUILD_PROJECT_NAME} LANGUAGES C CXX)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED
  )

set(CYTHON cython)
message(STATUS "Cython: " ${CYTHON})
#Test if cython is installed
if(NOT CYTHON)
  message(
    FATAL_ERROR
      "Cython is required to build Parla. Please install cython and try again."
    )
endif()
#Test if cython exists
execute_process(COMMAND ${CYTHON} --version ERROR_QUIET OUTPUT_VARIABLE CYTHON_VERSION)
if(NOT CYTHON_VERSION)
  message(
    FATAL_ERROR
      "Cython is required to build Parla. Please install cython and try again."
    )
endif()

message(STATUS "Python: " ${Python_EXECUTABLE})
include_directories(${NUMPY_INCLUDE})

set(CYTHON_FLAGS "--cplus;--fast-fail")

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
  set(PARLA_DEBUG_C_COMPILE_FLAGS "-fno-omit-frame-pointer")
  set(PARLA_DEBUG_CYTHON_FLAGS "--line-directives;-p;--gdb")

  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${PARLA_DEBUG_C_COMPILE_FLAGS}")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${PARLA_DEBUG_C_COMPILE_FLAGS}")
  list(APPEND CYTHON_FLAGS ${PARLA_DEBUG_CYTHON_FLAGS})
  list(APPEND CYTHON_FLAGS "-X;linetrace=True")
endif()

if(UNIX)
  if(APPLE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  else(NOT APPLE)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
  endif()
else(NOT UNIX)
  message(
    ERROR
    "Windows is not supported. Please raise an issue if you need Windows support."
  )
endif()

add_subdirectory(src/impl)
add_subdirectory(src/module)