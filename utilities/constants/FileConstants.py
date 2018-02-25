from os import path

PROJECT_ROOT_PATH = path.abspath('.')
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')

CMAKELISTS_INPUT_PATH = path.abspath('templates/CMakeLists.txt')
CMAKELISTS_FILENAME = 'CMakeLists.txt'

MAIN_CPP_INPUT_PATH = path.abspath('templates/main.cpp')
MAIN_CPP_FILENAME = 'main.cpp'