project(${project_name})
cmake_minimum_required(VERSION ${cmake_version})

set(PROJECT_ROOT $${PROJECT_SOURCE_DIR}/../..)
set(CMAKE_CXX_FLAGS "$${CMAKE_CXX_FLAGS} -std=${cpp_version}")

set(SRC_DIR $${PROJECT_ROOT}/src)
set(LIB_DIR $${PROJECT_ROOT}/lib)
set(TEST_DIR $${PROJECT_ROOT}/test)
set(INCLUDE_DIR $${PROJECT_ROOT}/include)

include_directories(
    $${INCLUDE_DIR}
)

add_executable(
    main
    $${SRC_DIR}/main.cpp
)