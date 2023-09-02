import os

def find_parentheses(folder_path, output_file):
    file_names = set()

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.js'):
                file_names.add(file_name)

    # Save file names to a text file
    output_path = os.path.join(output_file)
    with open(output_path, 'w') as file:
        for file_name in file_names:
            file.write(file_name + '\n')

    # print(f"File names saved to: {output_path}")



# Provide the folder path
folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated7\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js' + '\\'

# Provide the output directory path to save the CSV file
output_dir = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval\OutputFunctions' +'\\'+'outputItems.txt'

find_parentheses(folder_path, output_dir)

