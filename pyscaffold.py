from argparse import ArgumentParser
from os import path
from shutil import copytree, rmtree

from generators.project_gen import ProjectGenerator

from utilities.constants.file_constants import GENERATED_FILES_PATH

# TODO: Add flag for CMake project location.

parser = ArgumentParser(description = 'CMake C++ Project Generator written in Python 3')

parser.add_argument(
    '--project-name',
    action = 'store',
    default = 'SAMPLE_CMAKE_PROJECT'
)

parser.add_argument(
    '--cmake-version',
    action = 'store',
    default = '3.4.3'
)

parser.add_argument(
    '--cpp-version',
    action = 'store',
    default = 'c++14'
)

arguments = parser.parse_args()

project_generator = ProjectGenerator(arguments.__dict__)
project_generator.generate()

NEW_PROJECT_DIR = arguments.project_name

if not path.exists(NEW_PROJECT_DIR):
    copytree(GENERATED_FILES_PATH, arguments.project_name)

rmtree(GENERATED_FILES_PATH)