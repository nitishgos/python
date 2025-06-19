import os

# Specify the directory you want to list (you can change this to any valid path)
directory = "/"

try:
    # Get the list of files and directories
    contents = os.listdir(directory)

    # Print the contents
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")
