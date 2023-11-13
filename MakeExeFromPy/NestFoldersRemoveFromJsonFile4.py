import os
import json

def create_imports_json(starting_directory, custom_modules_directory, json_file_path):
    imports_dict = {}

    def process_file(file_path, parent_dict, processed_files):
        if file_path in processed_files:
            return

        processed_files.add(file_path)

        filesList = os.listdir(custom_modules_directory)
        with open(file_path, 'r') as f:
            content = f.read()
            imports = [line.split(' ')[1] for line in content.split('\n') if line.startswith('import') or line.startswith('from')]

            current_dict = {}
            parent_dict[file_path.replace(starting_directory,'').replace(".py",'').replace('\\','')] = current_dict

            for import_file in imports:
                import_path = os.path.join(os.path.dirname(file_path), import_file + '.py')
                if os.path.exists(import_path):
                    process_file(import_path, current_dict, processed_files)

    def process_directory(directory_path, parent_dict, processed_files):
        if directory_path in processed_files:
            return

        processed_files.add(directory_path)

        files = os.listdir(directory_path)

        for file in files:
            file_path = os.path.join(directory_path, file)

            if os.path.isdir(file_path):
                current_dict = {}
                parent_dict[file] = current_dict
                process_directory(file_path, current_dict, processed_files)
            elif file.endswith('.py'):
                process_file(file_path, parent_dict, processed_files)

    processed_files = set()
    process_directory(starting_directory, imports_dict, processed_files)

    with open(json_file_path, 'w') as json_file:
        json.dump(imports_dict, json_file, indent=2)

# Example usage:
starting_directory = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInput'
custom_modules_directory = starting_directory
json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson' + '\\' + 'imports.json'
create_imports_json(starting_directory, custom_modules_directory, json_file_path)
