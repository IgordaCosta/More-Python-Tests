from os import listdir
from os.path import isfile, join
import varInOnlyOneList
import getFirstFilePath




def FilesInOnlyOnePath(LessFilesPath,MoreFilesPath):

    LessFilesPathFiles = [f for f in listdir(LessFilesPath) if isfile(join(LessFilesPath, f))]

    MoreFilesPathFiles = [f for f in listdir(MoreFilesPath) if isfile(join(MoreFilesPath, f))]

    filePath = LessFilesPathFiles[0]

    FilePathOnly = getFirstFilePath.getFirstFilePath(filePath=filePath)


    ListOfFilesInOnlyOnePath = varInOnlyOneList.varInOnlyOneList(LessFilesList=LessFilesPathFiles,MoreFilesList=MoreFilesPathFiles)

    return ListOfFilesInOnlyOnePath, FilePathOnly