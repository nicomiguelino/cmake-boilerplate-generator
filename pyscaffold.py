from argparse import ArgumentParser
from generators.cmakelists_gen import CMakeListsGenerator
from generators.maincpp_gen import MainCppGenerator

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

cml_generator = CMakeListsGenerator(arguments.__dict__)
cml_generator.generate_file()

maincpp_generator = MainCppGenerator()
maincpp_generator.generate_file()