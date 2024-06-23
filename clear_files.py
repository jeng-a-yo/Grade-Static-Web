import os

def clear_directory(directory):
    # Get all files and directories within the specified directory
    all_files = os.listdir(directory)
    
    # Iterate through all files and directories
    for file_name in all_files:
        file_path = os.path.join(directory, file_name)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            try:
                # Remove the file
                os.remove(file_path)
                print(f"Removed file: {file_path}")
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")
        
        # If it's a directory, you can choose to remove its files as well
        # If you want to clear files within subdirectories, you can recursively call clear_directory()
        # else:
        #     clear_directory(file_path)

# Specify the directory path where files should be cleared
directory_to_clear = 'all_files'

# Call the function to clear all files within the directory
clear_directory(directory_to_clear)
