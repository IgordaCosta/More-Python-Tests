import os
import shutil

def get_file_names_in_directory(directory_path):
    # file_names0 = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    file_names = [file.replace('.py','.exe') for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
    # file_names = file_names0 + file_names1
    return file_names

def move_files_to_location(file_names, source_directory, destination_path):
    for file_name in file_names:
        source_file = os.path.join(source_directory, file_name)
        destination_file = os.path.join(destination_path, file_name)

        try:
            shutil.copy(source_file, destination_file)
            print(f"Moved '{source_file}' to '{destination_path}'")
        except FileNotFoundError:
            print(f"File '{file_name}' not found in the source directory.")
        except shutil.Error as e:
            print(f"Error moving '{source_file}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

source_directory = r'F:\Stuff\PythonFilesIntoExes\B_ToCopyFromLocation'
destination_path = r'F:\Stuff\PythonFilesIntoExes\B_CopyToLocation'
source_directory_names = r'F:\Stuff\PythonFilesIntoExes\B_ToCopyGuide'

if not os.path.exists(destination_path):
    os.makedirs(destination_path)

file_names = get_file_names_in_directory(source_directory_names)

if file_names:
    print("Files in the source directory:")
    for file_name in file_names:
        print(file_name)

    move_files_to_location(file_names, source_directory, destination_path)
else:
    print("No files found in the source directory.")




# print(['a','b','c']+[1,2,3])