import os
import chardet



import re
import glob

def remove_html_comments(html_code):
    # Uncomment the line or multiline comment with dragnDrop2()
    pattern = r"<!--\s*<script>\s*DragnDrop2\(\)\s*<\/script>\s*-->"
    html_code = re.sub(pattern, r"<script>DragnDrop2()</script>", html_code, flags=re.DOTALL)
    
    # Remove other multiline comments
    pattern = r"<!--[\s\S]*?-->"
    html_code = re.sub(pattern, '', html_code)
    
    # Remove other single-line comments
    pattern = r"<!--.*?-->"
    html_code = re.sub(pattern, '', html_code)
    
    return html_code

def remove_comments_in_folder(folder_path):
    # Get all HTML files in the folder
    html_files = glob.glob(os.path.join(folder_path, "*.html"))
    
    for file in html_files:
        with open(file, 'r') as f:
            html_code = f.read()
        
        # Remove comments from HTML code
        clean_html = remove_html_comments(html_code)
        
        with open(file, 'w') as f:
            f.write(clean_html)
        
        print(f"Comments removed from {file}")





#########################################################3
import os
import chardet

def detect_encoding(filename):
    with open(filename, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']

def join_lines(filename):
    lines = []
    joined_lines = []
    encoding = detect_encoding(filename)
    
    with open(filename, 'r', encoding=encoding, errors='replace') as file:
        lines = file.readlines()

    i = 0
    while i < len(lines) - 1:
        line = lines[i].rstrip()
        next_line = lines[i + 1].rstrip()

        if line == '</div>' and next_line == '</body>':
            joined_lines.append('<script type="text/javascript" src="./js/DragnDrop2.js"></script>\n')
            joined_lines.append(line + '\n')
            joined_lines.append(next_line + '\n')
            i += 2
        else:
            joined_lines.append(line + '\n')
            i += 1

    joined_lines.extend(lines[i:])

    with open(filename, 'w', encoding=encoding) as file:
        file.writelines(joined_lines)

def remove_lines_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            filtered_lines = [line for line in lines if not ('DragnDrop2()' in line.rstrip())]

            with open(file_path, 'w') as file:
                file.writelines(filtered_lines)

            join_lines(file_path)

            print(f"Lines removed successfully in '{filename}'")

# Prompt the user to enter the folder path


folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\'




remove_comments_in_folder(folder_path)

remove_lines_in_folder(folder_path)
