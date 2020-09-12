import os.path

import FixExcelExtension



def CheckIfFileInFonder(folder,file):

    file=FixExcelExtension.FixExcelExtension(fileName=file)

    finalPath=os.path.join(folder,file)

    FileExists=os.path.exists(finalPath)

    return FileExists







