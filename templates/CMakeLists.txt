project(${project_name})
cmake_minimum_required(VERSION ${cmake_version})

set(PROJECT_ROOT $${PROJECT_SOURCE_DIR}/../..)
set(CMAKE_CXX_FLAGS "$${CMAKE_CXX_FLAGS} -std=${cpp_version}")

set(SRC_DIR $${PROJECT_SOURCE_DIR}/src)
set(LIB_DIR $${PROJECT_SOURCE_DIR}/lib)
set(TEST_DIR $${PROJECT_SOURCE_DIR}/test)
set(INCLUDE_DIR $${PROJECT_SOURCE_DIR}/include)

include_directories(
    $${INCLUDE_DIR}
)

add_executable(
    main
    $${SRC_DIR}/main.cpp
)