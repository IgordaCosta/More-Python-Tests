import os

def process_folder(folder_path, input_file_path, output1_path, output2_path, output3_path):
    ignored_items = read_ignored_items(input_file_path)
    folder_names = get_folder_names(folder_path)
    
    items_not_in_folder = ignored_items.difference(folder_names)
    folder_names_not_in_items = folder_names.difference(ignored_items)
    items_in_both = ignored_items.intersection(folder_names)

    write_items(items_not_in_folder, output1_path)
    write_items(folder_names_not_in_items, output2_path)
    write_items(items_in_both, output3_path)

def read_ignored_items(input_file_path):
    ignored_items = set()

    with open(input_file_path, "r") as file:
        for line in file:
            ignored_items.add(line.strip())

    return ignored_items

def get_folder_names(folder_path):
    folder_names = set()

    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            name_without_extension = os.path.splitext(filename)[0]
            folder_names.add(name_without_extension)

    return folder_names

def write_items(items, output_file_path):
    with open(output_file_path, "w") as file:
        for item in items:
            file.write(item + "\n")



# Usage example

FolderLocation =  r"C:\Users\Tigereye\Desktop\ImportPythonSaveLocations" + '\\'
folder_path = FolderLocation + "inputFiles"
input_file_path = FolderLocation + "input_file.txt"
not_in_folder_output_file_path = FolderLocation + "not_in_folder_output_file.txt"
not_in_txt_output_file_path = FolderLocation + "not_in_txt_output_file.txt"
common_output_file_path = FolderLocation + "common_output_file.txt"



output1_path = not_in_folder_output_file_path
output2_path = not_in_txt_output_file_path
output3_path =common_output_file_path

process_folder(folder_path, input_file_path, output1_path, output2_path, output3_path)



# # Usage example
# FolderLocation =  r"C:\Users\Tigereye\Desktop\ImportPythonSaveLocations" + '\\'
# folder_path = FolderLocation + "outputLocaion"
# input_file_path = FolderLocation  + "/input_file.txt"
# output_file_path = FolderLocation  + "/output_filevalid.txt"
# # ignored_output_file_path = FolderLocation  + "/output_fileignored.txt"


# process_folder(folder_path, input_file_path, output_file_path)


# # process_folder(folder_path, input_file_path, valid_output_file_path, ignored_output_file_path)
