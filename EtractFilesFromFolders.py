import shutil
import os


OutPutExtractedFilesFolderLocation = r'C:\Users\Dogman\Desktop\OutputExtractedFilesFolder' + '\\'

ImputToGetFoldersFrom = r'C:\Users\Dogman\Desktop\FolderToExtractFrom' + '\\'



FolderLocationsList= []
for Infolder in os.listdir(ImputToGetFoldersFrom):
    InItem = ImputToGetFoldersFrom + Infolder
    
    if os.path.isdir(InItem):
        FolderLocationsList.append(InItem)


# print(FolderLocationsList)


for pathInFolder in FolderLocationsList:

    FolderItens = os.listdir(pathInFolder)

    for item in FolderItens:
        # print(item)

        InputLocationFinal = pathInFolder +'\\' + item

        # print(InputLocationFinal)

        OutputLocationFinal = OutPutExtractedFilesFolderLocation + item

        # print(OutputLocationFinal)
        # print('+++++++++++++++++++++++++++')

        shutil.copyfile(InputLocationFinal, OutputLocationFinal)


print('DONE')

       