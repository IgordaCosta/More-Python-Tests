import os




def LocationFunctionJsFiles(folder_path, output_file, search_term):
    # Open the output file for writing
    with open(output_file, "w") as f:
        # Loop through all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Check if the file is a JS file
                if file.endswith(".js"):
                    # Open the file for reading
                    with open(os.path.join(root, file), "r") as js_file:
                        # Loop through all lines in the file
                        for line_num, line in enumerate(js_file):
                            # Check if the line contains the search term
                            if not '\\' in line:
                                if search_term in line:
                                    # Write the file name, line number, and line to the output file
                                    f.write(f"{file} _____ {line_num} _____ {line}")
                f.write('\n')






# Define the folder to search for JS files
folder_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\AllNewJsFilesWithoutComments\JsFilesWithoutComments2' +'\\'

# Define the output file for the results
output_file = r'C:\Users\Tigereye\Desktop\HTMLfiles\AllNewJsFilesWithoutComments\LocationOfFunctionsJsFiles' + '\\' + 'LocationOfFunctionsJsFiles.txt'

# Define the search term to look for in the JS files
search_term = "function"

LocationFunctionJsFiles(folder_path, output_file, search_term)