import os
import shutil

def GetFileNameFromTxtThenCopy(txt_file_list_path, file_location, dest_folder):
    # Check if destination folder exists, create it if it doesn't exist
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    # Open the txt file containing the list of filenames to copy
    with open(txt_file_list_path, 'r') as file_list:
        # Loop through each filename in the txt file
        for filename in file_list:
            # Strip whitespace and newlines from filename
            filename = filename.strip()
            
            # Create absolute path to source file
            abs_path = os.path.join(file_location, filename)

            # Check if source file exists
            if os.path.exists(abs_path):
                # Create absolute path to destination file
                dest_file = os.path.join(dest_folder, filename)

                # Copy file to destination folder
                shutil.copy(abs_path, dest_file)

                # Print success message
                # print(f"File '{filename}' successfully copied to '{dest_folder}'.")
            # else:
            #     # Print error message
            #     print(f"File '{filename}' does not exist at '{file_location}'.")

    print('DONE')




# textFilName = 'JsFunctionsFilesInHtml0.txt'
# textFilName = 'PyFunctionFilesInJsFile0.txt'
textFilName = 'PyFunctionFilesInJsFile0.txt'

# txt file containing the filenames to copy
# txt_file_list_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\PyFunctionFilesInJsFile' + '\\' + textFilName
# txt_file_list_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\JSFunctionfiles' + '\\' + textFilName
txt_file_list_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\pythonparts\1\PyFunctionFilesInPyFile' + '\\' + textFilName



# original file location
file_location = r'C:\Users\Tigereye\Desktop\HTMLfiles\partspy\1' +'\\'
# file_location = r'C:\Users\Tigereye\Desktop\HTMLfiles\ALLPyFileParts' +'\\'
# file_location = r'C:\Users\Tigereye\Desktop\JsFilesBackup20220413' +'\\'
# file_location = r'C:\Users\Tigereye\Desktop\FilteredJSFIles\1' + '\\'



# destination folder
# dest_folder = r'C:\Users\Tigereye\Desktop\HTMLfiles\JSFilesParts' + '\\'


# dest_folder =r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\js'

# dest_folder =r'C:\Users\Tigereye\Desktop\HTMLfiles\pythonparts' + '\\'

dest_folder =r'C:\Users\Tigereye\Desktop\HTMLfiles\pythonparts' + '\\'

GetFileNameFromTxtThenCopy(txt_file_list_path, file_location, dest_folder)