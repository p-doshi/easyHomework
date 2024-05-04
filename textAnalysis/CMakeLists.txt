cmake_minimum_required(VERSION 3.0)
project(textAnalysis)

# Add the source files
add_library(textAnalysisLib textAnalysis.cpp)

# Include the current directory for header files
target_include_directories(textAnalysisLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
