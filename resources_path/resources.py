import os
import tests


def resources_picture(file_names):
    return str(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), f'../picture/{file_names}')))

