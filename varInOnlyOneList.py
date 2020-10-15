







def varInOnlyOneList(LessFilesList, MoreFilesList):
    OnlyInOneListFiles = []
    for i in range(len(MoreFilesList)):
        if MoreFilesList[i] in LessFilesList:
            pass
        else:
            OnlyInOneListFiles.append(MoreFilesList[i])

    return OnlyInOneListFiles




# LessFilesList=['xcxcxcxcxcxz','sddfsdfsdff','gfhfghfghfghf',1,2,3,4,5]

# MoreFilesList=['xcxcxcxcxcxz','rtrtrtrtreeee','dfgdfgdfgdfg','jggfghfghfg','sddfsdfsdff','gfhfghfghfghf',0,1,2,3,4,5,6,7,8,9,10]

# OnlyInOneListFiles= varInOnlyOneList(LessFilesList, MoreFilesList)

# print(OnlyInOneListFiles)