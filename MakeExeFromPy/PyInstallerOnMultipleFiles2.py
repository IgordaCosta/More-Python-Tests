import os
import subprocess
import csv

def create_executables(src_folder, output_folder, spec_folder, error_log_file):
    # Ensure the output and spec folders exist
    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(spec_folder, exist_ok=True)

    # List all .py files in the source folder
    python_files = [file for file in os.listdir(src_folder) if file.endswith('.py')]

    python_filesSize = len(python_files)
    itemNumber = 0

    with open(error_log_file, 'w', newline='') as error_log:
        error_writer = csv.writer(error_log)
        error_writer.writerow(['File', 'Error Message'])

        for file in python_files:
            itemNumber = itemNumber + 1

            # Get the full path of the Python file
            src_file = os.path.join(src_folder, file)

            # Define the output executable filename without the '.py' extension
            output_name = os.path.splitext(file)[0]

            # Create the command to run PyInstaller
            spec_file = os.path.join(spec_folder, output_name + '.spec')
            command = [
                'pyinstaller',
                
                src_file          # The source Python file
            ]

            # Run PyInstaller and capture stderr
            result = subprocess.run(command, stderr=subprocess.PIPE)

            if result.returncode != 0:
                error_message = result.stderr.decode('utf-8').strip()
                error_writer.writerow([file, error_message])
                print(f'Error creating executable for {file}: {error_message}')
            else:
                print(f'Successfully created executable for {file} ({itemNumber}/{python_filesSize})')

source_folder = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesSelected' + '\\'
output_folder = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\ExesFileSelected' + '\\'
spec_folder = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\SpecFiles' + '\\'
error_log_file = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes' + '\\' + 'error_log.csv'

create_executables(source_folder, output_folder, spec_folder, error_log_file)

