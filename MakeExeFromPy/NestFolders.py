import os
import ast
import json

def get_imports_from_file(file_path):
    continuePart = False
    with open(file_path, 'r') as file:
        try:
            tree = ast.parse(file.read(), filename=file_path)
            continuePart = True
        except:
            pass
    if continuePart:
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                imports.add(node.module + '.' + node.names[0].name)

        return list(imports)

def get_all_imports(folder_path):
    all_imports = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports = get_imports_from_file(file_path)
                all_imports[file] = imports

    return all_imports

if __name__ == "__main__":
    folder_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInput' # Change this to the folder containing your Python files
    all_imports = get_all_imports(folder_path)

    print(all_imports)
    with open(r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson\imports.json', "w") as json_file:
        json.dump(all_imports, json_file, indent=2)

    print("Imports have been saved to 'imports.json'")
