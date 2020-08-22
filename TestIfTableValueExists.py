import getTableData


def TestIfTableValueExists(ValueToCheck,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):
    
    
    dictValue=getTableData.GetTableData(Database,TableName,ErrorIfNotFound,willChangeDirectory)

    print(dictValue)

    try:
        
        dictValue[ValueToCheck]
        print("the value exists")
        return True

    except KeyError:

        print("the value doese not exist")

        return False




ItExistsHere=TestIfTableValueExists(ValueToCheck='datafillName')


print(ItExistsHere)

print('ItExistsHere above')