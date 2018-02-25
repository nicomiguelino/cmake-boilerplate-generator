from os import chdir, mkdir, path
from string import Template

from utilities.constants.file_constants import *

class CMakeListsGenerator:
    def __init__(self, context):
        self.context = context

    def generate_file(self):
        if not path.exists(GENERATED_FILES_PATH):
            mkdir(GENERATED_FILES_PATH)

        with open(CMAKELISTS_INPUT_PATH, 'r') as input_file_handler:
            template_handler = Template(input_file_handler.read())
            template_output = template_handler.substitute(self.context)

            chdir(CMAKE_PROJECT_RELEASE_DIR)

            with open(CMAKELISTS_FILENAME, 'w') as output_file_handler:
                output_file_handler.write(template_output)