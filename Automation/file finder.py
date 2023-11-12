import os

def list_files(folder_path, output_file):
    with open(output_file, 'w') as output:
        for filename in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, filename)):
                output.write(filename + '\n')

if __name__ == "__main__":
    folder_path = './Images/Shdowgmes'  # Change this to the path of your folder
    output_file = 'file_names.txt'  # Change this to the desired output file name

    list_files(folder_path, output_file)
