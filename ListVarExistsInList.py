




def ListVarExistsInList(LessFilesList, MoreFilesList):

    ExistFilesList = []
    for i in range(len(LessFilesList)):
        if LessFilesList[i] in MoreFilesList:
            ExistFilesList.append(LessFilesList[i])

    return ExistFilesList


# LessFilesList=['xcxcxcxcxcxz','sddfsdfsdff','gfhfghfghfghf',1,2,3,4,5]

# MoreFilesList=['xcxcxcxcxcxz','rtrtrtrtreeee','dfgdfgdfgdfg','jggfghfghfg','sddfsdfsdff','gfhfghfghfghf',0,1,2,3,4,5,6,7,8,9,10]

# ExistFilesList= ListVarExistsInList(LessFilesList, MoreFilesList)

# print(ExistFilesList)