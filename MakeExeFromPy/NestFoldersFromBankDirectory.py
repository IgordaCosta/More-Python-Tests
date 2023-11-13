import os
import json
import shutil

def create_directories_from_json(json_file_path, base_directory, directory_bank):
    with open(json_file_path, 'r') as json_file:
        imports_dict = json.load(json_file)

    def create_directories_recursive(current_dict, current_path):
        i=0
        print(len(current_dict.items()))
        for key, value in current_dict.items():
            path = os.path.join(current_path, key)
            os.makedirs(path, exist_ok=True)

            # Copy directory structure from the bank
            bank_path = os.path.join(directory_bank, key)
            if os.path.exists(bank_path) and os.path.isdir(bank_path):
                shutil.copytree(bank_path, path, dirs_exist_ok=True)

            if isinstance(value, dict):
                create_directories_recursive(value, path)
            i=i+1
            print('++++++++ '+ str(i) + '/' + str(len(current_dict.items()))+' +++++++')

    create_directories_recursive(imports_dict, base_directory)

# Example usage:
json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson\imports.json'

# base_directory = r'F:\Stuff\PythonFilesIntoExes\C_OrganizeOutput'

base_directory = r'G:\C_OrganizeOutput'
directory_bank = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputFolders'

create_directories_from_json(json_file_path, base_directory, directory_bank)
print("++++++++++++++DONE++++++++++++++++")
