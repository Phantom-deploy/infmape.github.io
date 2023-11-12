import os

def find_main_folders(folder_path, output_file):
    # Check if the given path is a directory
    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a directory.")
        return

    # Get a list of all directories in the given path
    folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # Write folder names to the output file
    with open(output_file, 'w') as file:
        for folder in folders:
            file.write(folder + '\n')

    print(f"Main folders in '{folder_path}' written to '{output_file}'.")

# Example usage:
folder_path = '.\Shadowgmes'
output_file = 'names_output.txt'
find_main_folders(folder_path, output_file)
