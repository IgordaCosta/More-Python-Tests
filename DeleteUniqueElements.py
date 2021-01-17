import numpy


List=[1,2,3,2,3,4,5,2,6,6,7,8,9,2,0,3,0]

# a=[i for i in range(len(a)) if a.count(a[i])>1] # for index values

# a=[i for i in a if a.count(i)>1]  # to get the values themselves


# print(a)

def ListOfNonUniqueIndexValues(List):

    result=[i for i in range(len(List)) if List.count(List[i])>1]

    return result


def ListOfNonUniqueValues(List):

    result=[i for i in List if List.count(i)>1]

    return result




def ListOfOnlyTwoUniqueValues(List):
    ListOfTwoUnique = []

    for i in range(len(List)):
        if ListOfTwoUnique.count(List[i])<2:
            if List.count(List[i])>1:
                ListOfTwoUnique.append(List[i])

    return ListOfTwoUnique


def ListSelectedOrderUniqueValues(List):
    ListOfUnique = []

    ListOfUniqueIndex = []

    ListOfTwoUniqueCountOrder = []

    for i in range(len(List)):
        if List.count(List[i])>1:
            AmountInList=ListOfUnique.count(List[i])
            ListOfUnique.append(List[i])
            ListOfTwoUniqueCountOrder.append(AmountInList+1)

            ListOfUniqueIndex.append(i)
                


    return ListOfUnique, ListOfTwoUniqueCountOrder, ListOfUniqueIndex



def FilterListFromTwoComparingValues(First,Second,ValueGetList,CheckedList):

    EqualList=[]

    for i in range(len(ValueGetList)):
        Value = ValueGetList[i]

        if Value == First or Value == Second:
            EqualList.append(True)
        else:
            EqualList.append(False)

    # print(EqualList)

    npValueGetList =numpy.array(ValueGetList)

    npEqualList = numpy.array(EqualList)

    npCheckedList = numpy.array(CheckedList)

    ValueGetListChosen = npValueGetList[npEqualList]


    outputList = npCheckedList[npEqualList]

    return outputList, ValueGetListChosen






# First=1

# Second = 3


# CheckedList= ['god', 'car', 'beatle', 'bed', 'love', 'cat', 'deer', 'letter', 'read', 'sheep', 'bat']

# CompareList = [1, 1, 2, 2, 3, 1, 2, 4, 1, 3, 2]


# [2, 3, 2, 3, 2, 6, 6, 2, 0, 3, 0]
# [1, 1, 2, 2, 3, 1, 2, 4, 1, 3, 2]


# outputList = FilterListFromTwoComparingValues(First,Second,CompareList,CheckedList)

# print(outputList)






        






# result = ListOfOnlyTwoUniqueValues(List)


# result = ListOfNonUniqueIndexValues(List)

# result = ListOfNonUniqueValues(List)

# result1,result2 = ListSelectedOrderUniqueValues(List)

# print(result1)

# print(result2)


# print(list(result.values()))


# print(result[3])

