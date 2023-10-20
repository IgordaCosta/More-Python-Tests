import os
import shutil
import subprocess

# Set the source and target directories
source_dir = "/path/to/source_folder"
target_dir = "/path/to/target_folder"

# Ensure the target directory exists, or create it
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Iterate through the Python files in the source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".py"):
            # Create the target file name with .exe extension
            target_file = os.path.splitext(file)[0] + ".exe"
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_dir, target_file)

            # Use pyinstaller to convert the Python file to an executable
            subprocess.call(["pyinstaller", source_file_path, "--onefile"])

            # Move the generated executable to the target directory
            shutil.move(os.path.join(source_dir, "dist", target_file), target_file_path)

            # Clean up the temporary build directory created by pyinstaller
            shutil.rmtree(os.path.join(source_dir, "build"))
            shutil.rmtree(os.path.join(source_dir, "dist"))
            os.remove(os.path.join(source_dir, source_file_path + ".spec"))

print("Conversion to executable files is complete.")
