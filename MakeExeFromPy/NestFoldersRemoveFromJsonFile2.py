import os
import json

def create_imports_json(starting_directory, custom_modules_directory, json_file_path):
    imports_dict = {}

    def process_file(file_path):
        filesList = os.listdir(custom_modules_directory)
        # print(filesList)
        nonlocal imports_dict
        with open(file_path, 'r') as f:
            content = f.read()
            imports = [line.split(' ')[1] for line in content.split('\n') if line.startswith('import') or line.startswith('from')]

            # print(imports)
            # imports_dict[file_path] = [imp for imp in imports if os.path.join(custom_modules_directory, imp + '.py') == file_path]
            # print([imp for imp in imports if  imp + '.py' in filesList])

            # imports_dict[file_path] = [imp for imp in imports if  imp + '.py' in filesList]

            imports_dict[file_path.replace(starting_directory,'').replace(".py",'').replace('\\','')] = [imp for imp in imports if  imp + '.py' in filesList]
            for import_file in imports:
                import_path = os.path.join(os.path.dirname(file_path), import_file + '.py')
                if os.path.exists(import_path):
                    process_file(import_path)

    def process_directory(directory_path):
        files = os.listdir(directory_path)

        for file in files:
            file_path = os.path.join(directory_path, file)

            if os.path.isdir(file_path):
                process_directory(file_path)
            elif file.endswith('.py'):
                process_file(file_path)

    process_directory(starting_directory)

    with open(json_file_path, 'w') as json_file:
        json.dump(imports_dict, json_file, indent=2)

# Example usage:
# create_imports_json('/path/to/your/directory', '/path/to/custom/modules', 'imports.json')



starting_directory = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInput'

custom_modules_directory=starting_directory

json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson'+ '\\' + 'imports.json'

create_imports_json(starting_directory , custom_modules_directory, json_file_path)

# create_imports_json(starting_directory, json_file_path)
