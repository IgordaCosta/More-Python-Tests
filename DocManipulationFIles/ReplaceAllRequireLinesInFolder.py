import re
import os

def replace_require_lines_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".js"):
                full_path = os.path.join(root, filename)
                replace_require_lines(full_path)

def replace_require_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    # pattern = r'require\(\s*path\.join\((current(Directory|WorkingDirectory|WorkingPath)|CurrrentWorkingDirectory),\s*'
    pattern = r'require\(\s*path\.join\((currentWorkingDirectory),\s*'
    end_pattern = r'\s*\)\)'
    # patern2 = r'require('
    patern2 = 'dynamicRequire('

    for line in lines:
        if 'require(path.join(' in line:
        # if 'require(' in line:
            # modified_line= line
            modified_line = re.sub(pattern, patern2, line, flags=re.IGNORECASE)
            modified_line = re.sub(end_pattern, ')', modified_line)
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)


folder_path = r"C:\Users\Tigereye\Desktop\js"  # Replace with the path to your folder
replace_require_lines_in_folder(folder_path)

print('DONE')


