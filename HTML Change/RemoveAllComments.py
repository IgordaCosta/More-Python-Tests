import os
import re
import pygments.lexers as lexers
from pygments.util import ClassNotFound

def remove_comments_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                remove_comments(file_path)
            except ClassNotFound:
                print(f"No lexer found for {file_path}. Skipping...")

def remove_comments(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    try:
        lexer = lexers.guess_lexer_for_filename(file_path, content)
        lexer_name = lexer.name.lower()

        if 'html' in lexer_name:
            # Remove HTML comments (<!-- ... -->)
            content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        elif 'javascript' in lexer_name:
            # Remove line comments (// ...)
            content = re.sub(r'//.*', '', content)
            # Remove block comments (/* ... */)
            content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        elif 'python' in lexer_name:
            # Remove line comments (# ...)
            content = re.sub(r'#.*', '', content)

        with open(file_path, 'w') as file:
            file.write(content)

    except ClassNotFound:
        print(f"No lexer found for {file_path}. Skipping...")



# Usage example
folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\js'
remove_comments_folder(folder_path)
