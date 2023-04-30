
def makeAllTxtVariablesUnique(FileLocation, filename,  new_filename):
    # Open the file and read the data into a list
    with open(FileLocation + filename, "r") as file:
        data = file.readlines()

    # Remove any whitespace or newline characters from the list
    data = [line.strip() for line in data]

    # Convert the list to a set and then back to a list
    data_set = set(data)
    new_data = list(data_set)

    # Write the new data to a new file

    with open(FileLocation + new_filename, "w") as file:
        for item in new_data:
            file.write("%s\n" % item)




#file name, new file, and location

filename = 'JsFunctionInJsFilesAll.txt'

new_filename = 'UniqueJsFunctionInJsFilesAll.txt'

FileLocation = r'C:\Users\Tigereye\Desktop\HTMLfiles\JSFunctionfiles\differentValues' +'\\'

makeAllTxtVariablesUnique(FileLocation ,filename,  new_filename)