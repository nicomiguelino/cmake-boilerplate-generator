from os import path

# CMakeLists.txt generator constants
PROJECT_ROOT_PATH = path.abspath('.')
CMAKELISTS_INPUT_PATH = path.abspath('templates/CMakeLists.txt')
CMAKELISTS_FILENAME = 'CMakeLists.txt'
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')

# main.cpp generator constants
PROJECT_ROOT_PATH = path.abspath('.')
MAIN_CPP_INPUT_PATH = path.abspath('templates/main.cpp')
MAIN_CPP_FILENAME = 'main.cpp'
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')