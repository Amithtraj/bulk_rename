import os

def rename_files(folder_path, remove_part):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through the files
    for file_name in files:
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(folder_path, file_name)):
            # Rename the file by removing the specified part
            new_name = file_name.replace(remove_part, '')
            
            # Construct the full paths for both old and new names
            old_path = os.path.join(folder_path, file_name)
            new_path = os.path.join(folder_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            
            print(f"Renamed '{file_name}' to '{new_name}'")

# Example Usage:
folder_path = r"C:\Users\USER\Desktop\Spotify"

remove_part = '[SPOTIFY-DOWNLOADER.COM] '

rename_files(folder_path, remove_part)
