import os

def replace_string_in_files(folder_path, old_string, new_string):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.js', '.html')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                content = content.replace(old_string, new_string)

                with open(file_path, 'w') as f:
                    f.write(content)

folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\js' + '\\'  # Replace with the actual folder path
old_string = 'id="this.parentElement.classList.add(\'hidden\')"'
new_string = 'id="closeButton"'

replace_string_in_files(folder_path, old_string, new_string)
