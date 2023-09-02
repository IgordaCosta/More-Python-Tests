import os
import chardet
import re

def replace_onclick(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.js'):
                file_path = os.path.join(root, file_name)

                with open(file_path, 'rb') as file:
                    raw_data = file.read()
                    encoding = chardet.detect(raw_data)['encoding']

                with open(file_path, 'r', encoding=encoding) as file:
                    lines = file.readlines()

                with open(file_path, 'w', encoding=encoding) as file:
                    print(file_path)
                    for line in lines:
                        new_line = re.sub(r'onclick\s*=\s*["\'](.*?)["\']', r'id', line)
                        file.write(new_line)

folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\js' + '\\'
replace_onclick(folder_path)
