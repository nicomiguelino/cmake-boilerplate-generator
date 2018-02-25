from os import chdir, mkdir, path
from utilities.constants.file_constants import GENERATED_FILES_PATH

TOPLEVEL_DIRECTORIES = ['build', 'include', 'lib', 'src', 'test']

# TODO: Make generation of project files manageable and dynamic.
# - A JSON/YAML file could be used as the blueprint, as they could represent hierarchies.
# - You could use tuples, lists, or dictionaries as a temporary workaround.

class ProjectGenerator:
    def __init__(self, project_name):
        self.project_name = project_name

    def generate(self):
        if not path.exists(GENERATED_FILES_PATH):
            mkdir(GENERATED_FILES_PATH)

        chdir(GENERATED_FILES_PATH)

        for directory in TOPLEVEL_DIRECTORIES:
            if not path.exists(directory):
                mkdir(directory)

        chdir('build')

        if not path.exists('release'):
            mkdir('release')