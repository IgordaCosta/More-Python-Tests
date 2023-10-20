import os

def add_comment_to_print_statements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if 'print' in line and not line.strip().startswith('#'):
            line = '#' + line

        modified_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def process_files_in_folder(folder_path, ignore_filename):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py') and file_name != ignore_filename:
                file_path = os.path.join(root, file_name)
                add_comment_to_print_statements(file_path)

if __name__ == "__main__":
    folder_path = '/path/to/your/folder'  # Replace with the path to your folder
    ignore_filename = 'filename_to_ignore.py'  # Replace with the filename you want to ignore
    process_files_in_folder(folder_path, ignore_filename)
