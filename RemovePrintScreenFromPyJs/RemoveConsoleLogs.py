import os
import re

def comment_out_console_logs(folder_path):
    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                
                modified_lines = []
                in_comment_block = False

                for line in lines:
                    # Check if the line contains "console.log("
                    if 'console.log(' in line:
                        # Check if "//" is already in front of the line
                        if not re.match(r'\s*//', line):
                            # If not, add "//" in front of it
                            line = '//' + line

                    # Handle multi-line comment blocks
                    if '/*' in line:
                        in_comment_block = True
                    if '*/' in line:
                        in_comment_block = False

                    if in_comment_block:
                        line = '//' + line

                    modified_lines.append(line)

                with open(file_path, 'w') as f:
                    f.writelines(modified_lines)


folder_path = r'C:\Users\Tigereye\Desktop\Stuff\ChangedJsFiles' + '\\'
comment_out_console_logs(folder_path)
print("console.log statements have been commented out in JavaScript files.")
