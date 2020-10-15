






def getFirstFilePath(filePath):
    FistFile0=filePath

    FistFile = FistFile0.replace('\\', '//')

    PathOfFile0 = FistFile.split('//')

    Filename = PathOfFile0[-1]

    FistFilePath = FistFile0.replace(Filename, '')

    return FistFilePath




# filePath='C://Users//IgorDC//Documents\\WindowsPowerShell//filenameusedfortest.txt'

# FilePath = getFirstFilePath(filePath)


# print(FilePath)