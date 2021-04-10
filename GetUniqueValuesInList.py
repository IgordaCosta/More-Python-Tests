


def GetUniqueValuesInList(List):

    # result=[i for i in List if List.count(i)==1]
    ResultList = []
    for i in range(len(List)):
        if List.count(List[i])==1:
            ResultList.append(True)

        else:
            ResultList.append(False)


    return ResultList







# List = [5,2,3,1,4,5]



# resultList = GetUniqueValuesInList(List)

# print(resultList)