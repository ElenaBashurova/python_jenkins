import os
import tests_demoqa


def resources_picture(file_names):
    return str(
        os.path.abspath(
            os.path.join(os.path.dirname(tests_demoqa.__file__), f'../picture/{file_names}')))

