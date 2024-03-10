import environment_manager
import os

def find_directory(dir_name):
    """
    Find a directory with the specified name in the parent directory of this script.
    """

    script_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(script_directory)

    if environment_manager.env == "LOCAL":
        print("Current Working Directory:", os.getcwd())
        print("Script Directory:", script_directory)
        print("Parent Directory:", parent_directory)
        print("Directories in Parent Directory:", os.listdir(parent_directory))

    for subdir in os.listdir(parent_directory):
        if subdir == dir_name:
            return os.path.join(parent_directory, subdir)
    return None