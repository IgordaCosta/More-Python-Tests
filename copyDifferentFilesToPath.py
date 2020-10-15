import shutil

import FilesInOnlyOnePath



def copyDifferentFilesToPath(NewFileLocation,LessFilesPath,MoreFilesPath):

    ListOfFilesInOnlyOnePath, FilePathOnly = FilesInOnlyOnePath.FilesInOnlyOnePath(LessFilesPath=LessFilesPath,MoreFilesPath=MoreFilesPath)

    for i in range(len(ListOfFilesInOnlyOnePath)):

        newPath = shutil.copy(FilePathOnly + ListOfFilesInOnlyOnePath[i],NewFileLocation + ListOfFilesInOnlyOnePath[i] )

        print(newPath)

    print('Done')