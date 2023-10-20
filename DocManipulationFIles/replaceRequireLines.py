import re

def replace_require_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    pattern = r'\s*path\.join\(currentWorkingDirectory,\s*'
    end_pattern = r'\s*\)\s*\)'

    for line in lines:
        modified_line = re.sub(pattern, '', line, flags=re.IGNORECASE)
        modified_line = re.sub(end_pattern, ')', modified_line)
        modified_lines.append(modified_line)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)


folderLocation = r'C:\Users\Tigereye\Desktop\js'
filename = folderLocation + '\\' + "CheckIfNameExists.js"  # Replace with the path to your file
replace_require_lines(filename)
print("DONE")



# pattern = r'\s*path\.join\(currentWorkingDirectory,\s*'
