





def CreateEqualSizeList(InputList):

    InputListSizeAfter = len(InputList) - 1

    OutputList = []

    OutputList2 = []
    for i in range(InputListSizeAfter):

        colname = '-'
        datatype = 'TEXT'

        itemToAppend = [colname , datatype]



        OutputList.append(itemToAppend)

        OutputList2.append(colname)

    return OutputList, OutputList2


# InputList2 = [1,2,3,4]

# print(CreateEqualSizeList(InputList = InputList2))