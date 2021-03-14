###### this gets the list of file lines one by one and cretes a python list object
###### this list object will be returned in the function and used in a for loop
###### for blocking all office exe files from access inside and outside the firewall





def getListFromtxtfile(Location, fileName):
    ListGotten = open(Location + fileName).readlines()

    return ListGotten



# Location = r'C:\Users\IgorDC\Desktop\PydocTest' + '\\'

# fileName = 'officeFileExeLocations.txt'


# ListGotten = getListFromtxtfile(Location, fileName)

# print(ListGotten)