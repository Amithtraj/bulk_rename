# Description:

This Python script provides a utility for batch-renaming files within a specified folder. It takes two parameters: the folder path containing the files to be renamed, and a string pattern to be removed from the existing file names. The script checks if the specified folder path exists and, if so, iterates through the files, identifying regular files (not directories) and renaming them accordingly. The new names are constructed by removing the specified pattern, and the original files are replaced with the renamed versions. The script then prints out the details of each renaming operation.
Example Usage:

python

# Define folder path and pattern to remove
folder_path = r"C:\Users\USER\Desktop\Spotify"
\n
remove_part = 'unwated texts'

# Call the function to rename files
rename_files(folder_path, remove_part)

Note: Ensure to provide the correct folder path and pattern for successful execution.
