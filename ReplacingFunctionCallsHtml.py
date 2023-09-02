import os
import re


##### function OK
def transform_script_tags(html):
    
    if "<script" in html:
        # print(html)
        html = html.replace(';', '')

    pattern = r'<script>\s*(.*?)\(\)\s*</script>'
    replacement = r'<script src="./js/\1.js"></script>'
    transformed_html = re.sub(pattern, replacement, html)
    return transformed_html

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.html') or filename.endswith('.js'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                html = file.read()
                transformed_html = transform_script_tags(html)
            with open(file_path, 'w') as file:
                file.write(transformed_html)


folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\js' '\\'
process_folder(folder_path)
# process_folder(folder_path)

