import os




def LocationFunctionJsFiles(folder_path, output_file, search_term, BlockItem,FileExtentionToSearch):
    # Open the output file for writing
    with open(output_file, "w") as f:
        # Loop through all files in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Check if the file is a JS file
                if file.endswith(FileExtentionToSearch):
                    # Open the file for reading
                    with open(os.path.join(root, file), "r") as js_file:
                        # Loop through all lines in the file
                        for line_num, line in enumerate(js_file):
                            # Check if the line contains the search term
                            # if not '\\' in line:
                            #     if not 'function ' in line:
                            #         if not 'cwd' in line:
                            #             if not '[' in line:
                            #                 if not '<' in line:
                            #                     if not 'holder.' in line:
                                                    if not BlockItem in file:
                                                        if search_term in line:
                                                            # Write the file name, line number, and line to the output file
                                                            f.write(f"{file} _____ {line_num} _____ {line}")
                f.write('\n')






# Define the folder to search for text files
# folder_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\partspy\1' +'\\'


folder_path =  r'C:\Users\Tigereye\Desktop\HTMLfiles\FunctionsToCheckForParts' +'\\'

# Define the output file for the results
output_file = r'C:\Users\Tigereye\Desktop\HTMLfiles\pythonparts\1\PyFunctionFilesInPyFile' + '\\' + 'LocationOfText.txt'

# Define the search term to look for in the JS files
# search_term = "()"
search_term = "location.replace"
BlockItem = "//"
FileExtentionToSearch = '.js'

LocationFunctionJsFiles(folder_path, output_file, search_term, BlockItem,FileExtentionToSearch)