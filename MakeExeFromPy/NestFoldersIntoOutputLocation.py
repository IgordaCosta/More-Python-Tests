import os
import json
import shutil

def copy_folders_from_json(json_file, source_folder, output_folder):
    with open(json_file, 'r') as file:
        all_imports = json.load(file)

    for file_name, imports in all_imports.items():
        # Check if the folder exists in the source folder
        source_folder_path = os.path.join(source_folder, os.path.dirname(file_name))
        if os.path.exists(source_folder_path):
            current_path = output_folder
            for imp in imports:
                sanitized_imp = sanitize_folder_name(imp)
                current_path = os.path.join(current_path, sanitized_imp)
                if not os.path.exists(current_path):
                    os.makedirs(current_path)

            destination_folder_path = os.path.join(current_path, os.path.basename(source_folder_path))
            
            # Using shutil.copytree to recursively copy the entire directory
            shutil.copytree(source_folder_path, destination_folder_path, dirs_exist_ok=True)

def sanitize_folder_name(name):
    # Replace or remove invalid characters from the folder name
    sanitized_name = name.replace(".", "").replace("*", "").replace(":", "").replace("?", "").replace("\\", "").replace("/", "")
    return sanitized_name

if __name__ == "__main__":
    json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson\imports.json'
    source_folder = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInput'  # Change this to the source folder containing the directories to copy
    output_folder = r'F:\Stuff\PythonFilesIntoExes\C_OrganizeOutput'  # Change this to the desired output folder

    copy_folders_from_json(json_file_path, source_folder, output_folder)

    print("Folders have been copied according to the JSON structure.")
