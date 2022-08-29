from pysqlitecipher import sqlitewrapper


import CreateEqualSizeList


password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'

dataBasePath="pysqlitecipher.db"

tableName = 'testTable'

iDValue = 0



colNameList = ['colNameTest1',]

colValueList = ['NewValue1',]

obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)

print(obj)



datatype = 'TEXT'

TableExist = False
try:
    TableData = obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False)
    TableExist = True
except Exception as e:
    WholeExeption = str(e)

    importantPartException = WholeExeption.split(',')[-1]

    if importantPartException == ' no such table in data base':
        print('This table Does not exist yet')





if TableExist:
    InputList = TableData[0] + colNameList
    colList, colList2 = CreateEqualSizeList.CreateEqualSizeList(InputList=InputList)

else : 
    colList2 = colNameList

    print(colNameList)

    colList = []
    for i in range(len(colNameList)):
        print(colNameList[i])
        colList.append([colNameList[i], datatype ])


print(colList)
print(colList2)


TableCreated = False
try:
    obj.createTable(tableName = tableName , colList = colList , makeSecure=False , commit=True)
    colList, colList2 = CreateEqualSizeList.CreateEqualSizeList(InputList=colList)
    TableCreated =True
except Exception as e:
    if str(e) == 'table name already exist in data base':
        print('Table already created')


if TableCreated:
    # print('DOne')

    # TableData0 = obj.describeTable(tableName)

    # print(TableData0)

    # TableData = obj.getDataFromTable(tableName , raiseConversionError = True , omitID = True)

    # print(TableData)

    # print(len(TableData))

    # print(TableData[0])

    # print(TableData[0][1])

    insertList = colList2

    # iDValue = 0

    # try:
    #     obj.deleteDataInTable(tableName , iDValue , commit = True , raiseError = True , updateId = True)
    # except Exception as e:
    #     if str(e) == 'ID = 0 not found while deletion process':
    #         print('ID does not exist')

    obj.insertIntoTable(tableName=tableName , insertList=insertList , commit = True)

    # colName = colname

    # colValue = 'TestValue1'

    for i in range(len(colNameList)):


        obj.updateInTable(tableName , iDValue , colName= colNameList[i] , colValue = colValueList[i] , commit = True , raiseError = True)

    TableData2 = obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False)
    print(TableData2)


else:
    print('Table already exist and now must append')

    TableDataToAppend = obj.getDataFromTable(tableName , raiseConversionError = True , omitID = True)
    print(TableDataToAppend)

    # print(TableDataToAppend[0])

    print(TableDataToAppend[1])
    print(TableDataToAppend[1][0])

    colNameList2 = TableDataToAppend[0] + colNameList

    colValueList2 = TableDataToAppend[1][0] + colValueList

    print(colNameList2)
    print(colValueList2)

    colList2 = []
    for i in range(len(colNameList2)):
        print(colNameList2[i])
        colList2.append([colNameList2[i], datatype ])

    print(colList2)

    # colList, colList2 = CreateEqualSizeList.CreateEqualSizeList(InputList=colList)

    # insertList = colList2

    



    obj.insertIntoTable(tableName=tableName , insertList=colNameList , commit = True)


    # for i in range(len(colNameList2)):


    #     obj.updateInTable(tableName , iDValue , colName= colNameList2[i] , colValue = colValueList2[i] , commit = True , raiseError = True)

    TableData2 = obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False)
    print(TableData2)