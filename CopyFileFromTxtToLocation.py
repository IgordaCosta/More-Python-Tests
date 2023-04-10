import os
import shutil




#the txt file containing the filenames to copy
file_list_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\JSfilesFromJS' + '\\' + 'JsFilesInJsInAppALL0.txt'

#original file location
file_location = r'C:\Users\Tigereye\Desktop\HTMLfiles\SavedJsFiles' +'\\'

#destination folder
dest_folder =  r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\CSSAutoFormFiller\js' + '\\'

# Check if destination folder exists, create it if it doesn't exist
if not os.path.exists(dest_folder):
    os.mkdir(dest_folder)

# Open the txt file containing the list of filenames to copy
with open(file_list_path, 'r') as file_list:
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
        else:
            # Print error message
            # print(f"File '{filename}' does not exist at '{file_location}'.")
            pass

print('DONE')