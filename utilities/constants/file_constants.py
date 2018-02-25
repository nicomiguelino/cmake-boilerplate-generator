from os import path

PROJECT_ROOT_PATH = path.abspath('.')
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')

CMAKELISTS_INPUT_PATH = path.abspath('templates/CMakeLists.txt')
CMAKELISTS_FILENAME = 'CMakeLists.txt'

MAIN_CPP_INPUT_PATH = path.abspath('templates/main.cpp')
MAIN_CPP_FILENAME = 'main.cpp'

CMAKE_PROJECT_BUILD_DIR = path.join(GENERATED_FILES_PATH, 'build')
CMAKE_PROJECT_RELEASE_DIR = path.join(CMAKE_PROJECT_BUILD_DIR, 'release')
CMAKE_PROJECT_SRC_DIR = path.join(GENERATED_FILES_PATH, 'src')