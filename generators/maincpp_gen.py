from os import chdir, mkdir, path
from string import Template

from utilities.constants.file_constants import *

class MainCppGenerator:
    def __init__(self):
        self.context = dict()

    def generate(self):
        if not path.exists(GENERATED_FILES_PATH):
            mkdir(GENERATED_FILES_PATH)

        with open(MAIN_CPP_INPUT_PATH, 'r') as input_file_handler:
            template_handler = Template(input_file_handler.read())
            template_output = template_handler.substitute(self.context)

            chdir(CMAKE_PROJECT_SRC_DIR)

            with open(MAIN_CPP_FILENAME, 'w') as output_file_handler:
                output_file_handler.write(template_output)

        # TODO: Create a function wrapper and add this action to the wrapper.
        chdir(PROJECT_ROOT_PATH)