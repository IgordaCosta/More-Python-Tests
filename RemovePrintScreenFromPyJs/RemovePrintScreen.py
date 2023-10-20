import os

def search_and_comment_prints(folder_path, ignore_filename):
    files = os.listdir(folder_path)
    for filename in files:
        if filename == ignore_filename:
            pass
        else:
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
            except UnicodeDecodeError:
                print(f"Skipping file {file_path} due to decoding error")
                continue

            modified_lines = []
            for line in lines:
                if 'print(' in line and not line.strip().startswith('#'):
                    line = '#' + line

                modified_lines.append(line)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)


folder_path = r'C:\Users\Tigereye\Desktop\Stuff\ChangedPythonFiles' + '\\'
ignore_filename = 'PrintTexListSerial.py' 
                                          

search_and_comment_prints(folder_path, ignore_filename)
print("Done!")
