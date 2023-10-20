import os

# Specify the directory where your Python files are located
directory = r"E:\Apps\CSSAutoFormFiller7_Updated94Cythonized\CSSAutoFormFiller\_engine\CythonFiles"

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        # Construct the old and new file paths
        old_path = os.path.join(directory, filename)
        new_filename = filename.replace('.py', '.pyx')  # Replace .py with .pyx
        new_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
