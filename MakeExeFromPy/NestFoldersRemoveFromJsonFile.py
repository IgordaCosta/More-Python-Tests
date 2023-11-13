# import json

# def get_py_files_from_json(json_file):
#     with open(json_file, 'r') as file:
#         all_items = json.load(file)

#     py_files = [file_name for file_name in all_items if ".py" in file_name]

#     return py_files

# if __name__ == "__main__":
#     json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson\imports.json'

#     py_files = get_py_files_from_json(json_file_path)

#     print("List of Python files in the JSON file:")
#     py_fileList = []
#     for py_file0 in py_files:
#         # py_file = py_file0.replace('.py', '')
#         # print(py_file)
#         py_fileList.append(py_file0)


#     with open(json_file_path, 'r') as file:
#         all_items = json.load(file)

#     # print(all_items.keys())

#     # allFolderKeys = all_items.keys().replace(".py", '')

#     py_files1 = [item.replace(".py", '') for item in all_items.keys() if item in py_fileList]
#     # py_files1 = [file_name for file_name in all_items.keys() if file_name in py_fileList]

#     # print(py_files1)


#     with open(json_file_path, 'r') as file:
#         all_items = json.load(file)

#     print(all_items.values())
    




import json

def get_py_files_from_json(json_file):
    with open(json_file, 'r') as file:
        all_items = json.load(file)

    py_files = [file_name for file_name in all_items if ".py" in file_name]

    return py_files

if __name__ == "__main__":
    json_file_path = r'E:\Stuff\PythonFilesIntoExes\C_OrganizedInputJson\imports.json'

    py_files = get_py_files_from_json(json_file_path)

    print("List of Python files in the JSON file:")
    py_fileList = [py_file.replace(".py", "") for py_file in py_files]
    print(py_fileList)

    with open(json_file_path, 'r') as file:
        all_items = json.load(file)

    # print(all_items.items())

    # print( {key: value for key, value in all_items.items() if value in all_items.values() in py_fileList}  )

    for item0 in all_items.items():
        print(item0)
        if item0 != None:
            print(item0)

                

        # for item1 in item0:
        #     print(item1)




    # # Filter items in all_items.values() that are not in py_files1
    # filtered_items = {key: value for key, value in all_items.items() if key.replace(".py", '') in py_fileList}

    # print(filtered_items)

    # # Update the JSON file with filtered items
    # with open(json_file_path, 'w') as file:
    #     json.dump(filtered_items, file, indent=2)

    # print("Filtered JSON file has been saved.")
