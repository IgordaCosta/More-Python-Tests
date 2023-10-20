import os
import shutil
import subprocess

# Set the source and target directories
source_dir = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesSelected'
target_dir = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesAll'

directory_path = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesSelected2' 

# Ensure the target directory exists, or create it
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# List of Python files to convert (specify their filenames)
# files_to_convert = ["file1.py", "file2.py", "file3.py"]

files_to_convert = [filename for filename in os.listdir(directory_path) if filename.endswith(".py")]

print(len(files_to_convert))

# Iterate through the specified Python files and convert them
for filename in files_to_convert:
    if filename.endswith(".py"):
        # Create the target file name with .exe extension
        target_file = os.path.splitext(filename)[0] + '.exe'
        source_file_path = os.path.join(source_dir, filename)
        target_file_path = os.path.join(target_dir, target_file)

        print(target_file)
        print('target_file')
        print(source_file_path)
        print('source_file_path')
        print(target_file_path)
        print('target_file_path')

        
        
        

        # Use pyinstaller to convert the Python file to an executable
        subprocess.call(["pyinstaller", source_file_path])

#         # Move the generated executable to the target directory
#         shutil.move(os.path.join(source_dir, "dist", target_file), target_file_path)

#         # Clean up the temporary build directory created by pyinstaller
#         shutil.rmtree(os.path.join(source_dir, "build"))
#         shutil.rmtree(os.path.join(source_dir, "dist"))
#         os.remove(os.path.join(source_file_path + ".spec"))

# print("Conversion to executable files is complete.")
