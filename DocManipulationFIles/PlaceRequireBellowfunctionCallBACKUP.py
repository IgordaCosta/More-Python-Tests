import os
import re

def replace_current_working_directory_in_folder(folder_path):
    # Define the pattern to search for
    pattern = r'require\(["\']path["\']\);'

    # Define the replacement text
var path = require("path");
const { requireModule } = require("./index"); // Require the function from the central module
const { customDirname } = require("./index");
const dynamicRequire = requireModule();
const { customDirname } = require("./index");
const dynamicRequire = requireModule();
const { customDirname } = require("./index");
const dynamicRequire = requireModule();
'''

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (not a subfolder)
        if os.path.isfile(file_path):
            # Read the contents of the file
            with open(file_path, 'r') as file:
                file_contents = file.read()

            # Use regular expressions to replace the pattern with the replacement text
            new_contents = re.sub(pattern, replacement, file_contents)

            # Write the modified contents back to the file
            with open(file_path, 'w') as file:
                file.write(new_contents)

# Example usage:
# Replace in all files within a folder named 'my_folder'
folderLocation = r'C:\Users\Tigereye\Desktop\js'
replace_current_working_directory_in_folder(folderLocation)


