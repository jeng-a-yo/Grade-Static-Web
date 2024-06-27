import os
import shutil
from timer import timing_decorator

@timing_decorator
def clear_directory(directory):
    try:
        # Iterate over all contents of the directory
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                # Remove files
                os.remove(file_path)
                print(f"Removed file: {file_path}")

            for name in dirs:
                dir_path = os.path.join(root, name)
                # Remove directories
                shutil.rmtree(dir_path)
                print(f"Removed directory: {dir_path}")

        print(f"All contents in directory '{directory}' have been cleared.")
    except Exception as e:
        print(f"Error clearing directory '{directory}': {e}")

# Specify the directory path where files and folders should be cleared
directory_to_clear = 'all_files'

# Call the function to clear all files and folders within the directory
clear_directory(directory_to_clear)
