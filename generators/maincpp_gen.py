from os import chdir, mkdir, path
from shutil import rmtree
from string import Template

PROJECT_ROOT_PATH = path.abspath('.')
MAIN_CPP_INPUT_PATH = path.abspath('templates/main.cpp')
MAIN_CPP_FILENAME = 'main.cpp'
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')

class FileMode:
    READ_ONLY = 'r'
    WRITE_ONLY = 'w'

class MainCppGenerator:
    def __init__(self):
        self.context = dict()

    def generate_file(self):
        with open(MAIN_CPP_INPUT_PATH, FileMode.READ_ONLY) as input_file_handler:
            template_handler = Template(input_file_handler.read())
            template_output = template_handler.substitute(self.context)

            if not path.exists(GENERATED_FILES_PATH):
                mkdir(GENERATED_FILES_PATH)

            chdir(GENERATED_FILES_PATH)

            with open(MAIN_CPP_FILENAME, FileMode.WRITE_ONLY) as output_file_handler:
                output_file_handler.write(template_output)