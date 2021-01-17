import getDirSize

def CheckIfAllDataCopied(folder1,folder2):
    start_path1 = folder1

    start_path2 = folder2

    pathsize1 = getDirSize.getDirSize(start_path1)
    # print('get_size(start_path1) bellow')
    # print(pathsize1)


    pathsize2 = getDirSize.getDirSize(start_path2)
    # print('get_size(start_path2) bellow')
    # print(pathsize2)

    FolderAreEqual = pathsize1==pathsize2
    # print('do they equal: ',str(FolderAreEqual))

    return FolderAreEqual, pathsize1, pathsize2





# folder1 = r'C:\Old PC'

# folder2 = r'D:\Old PC'




# FolderAreEqual, pathsize1, pathsize2= CheckIfAllDataCopied(folder1,folder2)


# print('FolderAreEqual: ',FolderAreEqual)

# print('pathsize1: ', pathsize1)

# print('pathsize2: ', pathsize2)