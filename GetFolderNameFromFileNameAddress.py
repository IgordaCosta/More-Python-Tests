


LocationToAddFileOnApp = 'C:/Users/Tigereye/Desktop/testDeleteFiles/filename.txt'

LocationToDeleteFIles = '\\'.join(LocationToAddFileOnApp.replace('/','\\').split('\\')[:-1]) + '\\'


print(LocationToDeleteFIles)