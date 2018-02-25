from argparse import ArgumentParser
from os import chdir, path
from shutil import copytree, rmtree

from generators.cmakelists_gen import CMakeListsGenerator
from generators.maincpp_gen import MainCppGenerator
from generators.project_gen import ProjectGenerator

from utilities.constants.file_constants import PROJECT_ROOT_PATH, GENERATED_FILES_PATH

# TODO: For each generator object's generate method, go to root dir. Use the TearDown technique. Use function wrappers.

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

# TODO: Encapsulate CMakeListsGenerator and MainCppGenerator inside ProjectGenerator as instance variables.

project_generator = ProjectGenerator(arguments.project_name)
project_generator.generate()

cml_generator = CMakeListsGenerator(arguments.__dict__)
cml_generator.generate()

maincpp_generator = MainCppGenerator()
maincpp_generator.generate()

# TODO: Copy generated files in current directory. Remove import and cd action later.

chdir(PROJECT_ROOT_PATH)

NEW_PROJECT_DIR = arguments.project_name

if not path.exists(NEW_PROJECT_DIR):
    copytree(GENERATED_FILES_PATH, arguments.project_name)

rmtree(GENERATED_FILES_PATH)