import os

def remove_newlines(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    for i in range(len(content)):
        line = content[i]
        if '<script>' in line.strip() and '\n' in line:
            content[i] = line.replace('\n', '')
        
    # last_line = content[-1].strip() if content else ""
    
    # if  "<script>" in last_line:
    for i in range(len(content)):
        line = content[i]
        if "<script>" in line:
            print(line )
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
            # if '()' in line.strip() and '\n' in line:
            #     content[i] = line.replace('\n', '')

    with open(filename, 'w') as file:
        file.writelines(content)

def process_js_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                remove_newlines(file_path)
                # print(f"Processed: {file_path}")

folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\'
process_js_files(folder_path)
