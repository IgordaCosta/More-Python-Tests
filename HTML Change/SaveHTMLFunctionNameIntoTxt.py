import os
import re

def extract_functions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    functions = []

    for line in lines:
        if "()" in line:
            line = line.replace("'", '"').split("(")[0].split('"')[-1]



            if "." in line:
                pass
            elif "=" in line:
                pass
            elif '--' in lines:
                pass
            elif str(line) == []:
                pass
            else:
                functions.append(str(line).replace('<script>', '').strip())

    return functions

def process_folder(folder_path, output_file_name):
    output_file = os.path.join(folder_path, output_file_name)

    functions1 = []
    with open(output_file, 'w') as file:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path) and filename != output_file_name:
                functions = extract_functions(file_path)

                functions1 = functions1 + functions

                functions1 = list(set(functions1))

        for function in functions1:
            file.write(function + '\n')

    print(f"Output written to {output_file}")

folder_path = r'C:\Users\Tigereye\Desktop\Stuff\FixCSPUnsafeEval' + '\\'
output_file_name =  'outuputFile.txt'
process_folder(folder_path, output_file_name)
