import os
import shutil



def DeleteAllJsBlockedlines(folder_path, destination_path):
    # Create the destination folder if it does not exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".js"): # Only process JS files
            file_path = os.path.join(folder_path, file_name)
            destination_file_path = os.path.join(destination_path, file_name)
            shutil.copyfile(file_path, destination_file_path) # Copy the file to the destination folder
            
            # Open the file and read all lines
            with open(destination_file_path, "r") as f:
                lines = f.readlines()
            
            # Open the file for writing and write only non-commented lines
            with open(destination_file_path, "w") as f:
                for line in lines:
                    line2 = line.replace(" ", '')
                    if not line2.startswith("//"):
                        if line2.strip() != '':
                            f.write(line)
    


# Replace with the path to your folder
folder_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\AllNewJsFilesWithoutComments\OriginalJSFiles'  + '\\'

# Replace with the path to your destination folder
destination_path = r'C:\Users\Tigereye\Desktop\HTMLfiles\AllNewJsFilesWithoutComments\JsFilesWithoutComments'  + '\\'

DeleteAllJsBlockedlines(folder_path, destination_path)