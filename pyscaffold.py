from argparse import ArgumentParser
from os import path
from shutil import copytree, rmtree

from generators.project_gen import ProjectGenerator

from utilities.constants.file_constants import GENERATED_FILES_PATH

# TODO: Convert Windows path format to Linux for consistency.

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

parser.add_argument(
    '--location',
    action = 'store',
    default = path.abspath('.')
)

arguments = parser.parse_args()

new_project_dir = path.join(arguments.location, arguments.project_name)

project_generator = ProjectGenerator(arguments.__dict__)
project_generator.generate()

print(new_project_dir)

if not path.exists(new_project_dir):
    copytree(GENERATED_FILES_PATH, new_project_dir)

rmtree(GENERATED_FILES_PATH)