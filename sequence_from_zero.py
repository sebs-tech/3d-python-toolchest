import os

def rename_files_in_directory(directory_path):
    # Get a list of files in the directory
    files = sorted(os.listdir(directory_path))
    
    # Iterate over the files and rename them
    for i, filename in enumerate(files):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Define the new file name with the current index and the original extension
        new_name = f"{i}{file_extension}"
        
        # Full old and new file paths
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")

# Specify the directory containing files you want to rename
directory_path = "/home/seb/hit/"
rename_files_in_directory(directory_path)


