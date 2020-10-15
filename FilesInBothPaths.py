from os import listdir
from os.path import isfile, join
import ListVarExistsInList




def FilesInBothPaths(LessFilesPath,MoreFilesPath):

    LessFilesPathFiles = [f for f in listdir(LessFilesPath) if isfile(join(LessFilesPath, f))]

    MoreFilesPathFiles = [f for f in listdir(MoreFilesPath) if isfile(join(MoreFilesPath, f))]


    ListOfFilesInBothPaths = ListVarExistsInList.ListVarExistsInList(LessFilesList=LessFilesPathFiles,MoreFilesList=MoreFilesPathFiles)

    return ListOfFilesInBothPaths