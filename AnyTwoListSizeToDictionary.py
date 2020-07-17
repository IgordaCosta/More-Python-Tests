
dataNameList=["a","b","c","d","e","f","g"]
dataList=[1,2,3,4,5,6,7]

Dictionary={"q":50,"r":70,"g":300}

for i in range(len(dataNameList)):
        Dictionary[dataNameList[i]]=dataList[i]


print(Dictionary)