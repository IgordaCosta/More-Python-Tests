import shutil
import os
import re
from os import listdir
from os.path import isfile, join

from itsdangerous import exc

ImputFolderFileLocation = r'C:\Users\Dogman\Desktop\DotTorrentFiles20220730' + '\\'

OutputFolderToFoldersLocation = r'C:\Users\Dogman\Desktop\SplitDotTorrentFiles' + '\\'



onlyfiles = [f for f in listdir(ImputFolderFileLocation) if isfile(join(ImputFolderFileLocation, f))]

# print(onlyfiles)


#================================================ test
firstFile = onlyfiles[0]

firstFileLocation = ImputFolderFileLocation + firstFile

#========================================================

# print(firstFileLocation)

# file = open(firstFileLocation, 'r')

# content = file.read()


# print(content)

for i in range(len(onlyfiles)):

    firstFile = onlyfiles[i]

    inputFileLocation = ImputFolderFileLocation + firstFile
    


    with open(inputFileLocation, encoding='latin-1') as file:
        content = file.read()

        contentList = content.split(':')

        # print(contentList[:5])
        # print(contentList[2:4])

        # print("_".join(contentList[2:4]))

        content2 = "_".join(contentList[2:4])

        
        content3 = re.sub("[^0-9a-zA-Z]", "_", content2)

        outputFileFolderLocation = OutputFolderToFoldersLocation + content3[7:47] + '\\' +  firstFile

        NewFolderLocationpath =  OutputFolderToFoldersLocation + content3[7:47] + '\\'

        try:
            os.makedirs(NewFolderLocationpath)
        except:
            pass

        # print('_________________________________________________________________')
        
        # print(inputFileLocation)
        # print(content3)
        # print(outputFileFolderLocation)
        # print('_________________________________________________________________')

        

        shutil.copyfile(inputFileLocation, outputFileFolderLocation)
    
print('DONE')