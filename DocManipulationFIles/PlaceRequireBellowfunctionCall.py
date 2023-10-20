import os

def process_files_in_folder(folder_path):
    # Define the text to append
    text_to_append = '''
let { requireModule } = require("./index"); // Require the function from the central module
let { customDirname } = require("./index");
let dynamicRequire = requireModule();
'''

    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the item is a file
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            # Open the input file and create an output file
            with open(file_path, 'r') as input_file, open(file_path + '.new', 'w') as output_file:
                for line in input_file:
                    # Check if the line starts with '//'
                    if line.strip().startswith('//'):
                        # Ignore the line
                        continue

                    # Check if the line contains 'var path = require("path");'
                    
                    if 'require("path")' in line:
                        # Append the desired text
                        output_file.write(line + text_to_append)
                    else:
                        # Write the original line
                        if "require('path')" in line:
                        # Append the desired text
                            output_file.write(line + text_to_append)
                        else:
                            # Write the original line
                            output_file.write(line)

                    


            # Replace the original file with the new one
            os.remove(file_path)
            os.rename(file_path + '.new', file_path)

            # print(f"Processed: {filename}")

# Example usage:
folderLocation = r'C:\Users\Tigereye\Desktop\js'
process_files_in_folder(folderLocation)
