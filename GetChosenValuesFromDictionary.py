

dictValue={'q': 50, 'r': 70, 'g': 7, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dataNameList=["q","b","f"]

Dictionary={}
for i in range(len(dataNameList)):
    data=dictValue[dataNameList[i]]
    Dictionary[dataNameList[i]]=data



print(Dictionary)