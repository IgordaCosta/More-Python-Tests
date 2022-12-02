


FolderTogoBackLocation = 'C:\\Users/Tigereye\\Documents\\AutoFormFillerFiles\\Temp\\temp_dadosMultaFacesIsabela_S8xLFDm.jpg'

NewLocation = '\\'.join(FolderTogoBackLocation.replace('/', '\\').split('\\')[:-2])

# print(NewLocation)

FileName = FolderTogoBackLocation.replace('/','\\').split('\\')[-1]

# print(FileName)

wholeLocaton = NewLocation + '\\' + FileName

# print(wholeLocaton)