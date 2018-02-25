from os import chdir, mkdir, path
from shutil import rmtree
from string import Template

PROJECT_ROOT_PATH = path.abspath('.')
CMAKELISTS_INPUT_PATH = 'templates/CMakeLists.txt'
CMAKELISTS_FILENAME = 'CMakeLists.txt'
GENERATED_FILES_PATH = path.join(PROJECT_ROOT_PATH, 'generated_files')

class FileMode:
    READ_ONLY = 'r'
    WRITE_ONLY = 'w'

class CMakeListsGenerator:
    def __init__(self, context):
        self.context = context

    def generate_file(self):
        with open(CMAKELISTS_INPUT_PATH, FileMode.READ_ONLY) as input_file_handler:
            template_handler = Template(input_file_handler.read())
            template_output = template_handler.substitute(self.context)

            if path.exists(GENERATED_FILES_PATH):
                rmtree(GENERATED_FILES_PATH)

            mkdir(GENERATED_FILES_PATH)
            chdir(GENERATED_FILES_PATH)

            with open(CMAKELISTS_FILENAME, FileMode.WRITE_ONLY) as output_file_handler:
                output_file_handler.write(template_output)