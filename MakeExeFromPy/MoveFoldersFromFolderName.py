import os
import shutil

def get_folder_names_in_directory(directory_path):
    print(os.listdir(directory_path))
    print(len(os.listdir(directory_path)))
    folder_names = [file.replace(".py", '') for file  in os.listdir(directory_path)]



    return folder_names

def move_folders_to_location(folder_names, source_directory, destination_path):
    for folder_name in folder_names:
        source_folder = os.path.join(source_directory, folder_name)
        print(source_folder)
        destination_folder = os.path.join(destination_path, folder_name)

        try:
            # shutil.copy(source_folder, destination_folder)
            shutil.copytree(source_folder, destination_folder)
            print(f"Moved '{source_folder}' to '{destination_path}'")
        except FileNotFoundError:
            print(f"Folder '{source_folder}' for '{source_folder}'not found in the source directory.")
        except shutil.Error as e:
            print(f"Error moving '{source_folder}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
source_directory = r'F:\Stuff\PythonFilesIntoExes\ToCopyFromLocation'
destination_path =r'F:\Stuff\PythonFilesIntoExes\CopyToLocation'

source_directory_names = r'F:\Stuff\PythonFilesIntoExes\PythonFilesSelected2\New folder'

# if not os.path.exists(destination_path):
#     os.makedirs(destination_path)

folder_names = get_folder_names_in_directory(source_directory_names)

print(folder_names)

if folder_names:
    print("Folders in the source directory:")
    for folder_name in folder_names:
        print(folder_name)

    move_folders_to_location(folder_names, source_directory, destination_path)
else:
    print(f"No folders found in the source directory.")
