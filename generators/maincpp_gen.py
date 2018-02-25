from os import chdir, mkdir, path
from string import Template

from utilities.constants.FileConstants import *

class MainCppGenerator:
    def __init__(self):
        self.context = dict()

    def generate_file(self):
        with open(MAIN_CPP_INPUT_PATH, 'r') as input_file_handler:
            template_handler = Template(input_file_handler.read())
            template_output = template_handler.substitute(self.context)

            if not path.exists(GENERATED_FILES_PATH):
                mkdir(GENERATED_FILES_PATH)

            chdir(GENERATED_FILES_PATH)

            with open(MAIN_CPP_FILENAME, 'w') as output_file_handler:
                output_file_handler.write(template_output)