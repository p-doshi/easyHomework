cmake_minimum_required(VERSION 3.0)
project(easyHomework)

# Main project code
find_package(cpprestsdk REQUIRED)

add_executable(main main.cpp)

include_directories(${cpprestsdk_INCLUDE_DIRS})

target_link_libraries(easyHomework PRIVATE ${cpprestsdk_LIBRARIES})

# Subdirectory code
add_subdirectory(/mnt/c/Users/Parth/OneDrive/Documents/easyHomework/easyHomework textAnalysisBuild)  # Provide a unique binary directory name
