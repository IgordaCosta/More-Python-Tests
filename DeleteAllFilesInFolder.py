import os
 

def DeleteAllFilesInFolder(LocationToDeleteFIles):
    for fileToDelete in os.listdir(LocationToDeleteFIles):
        os.remove(os.path.join(LocationToDeleteFIles, fileToDelete))
 

# LocationToDeleteFIles = r'C:\Users\Tigereye\Desktop\testDeleteFiles' +'\\'
# DeleteAllFilesInFolder(LocationToDeleteFIles)