from pysqlitecipher import sqlitewrapper

import os








# ItemNameList = ['Item1', 'Item2', 'Item3']       # item to add
# colValueList = ['NewValue5', 'NewValue6', 'NewValue8']    # item value






def WriteTableSecuredList(ItemNameList,colValueList):

    Database = 'fhjlasjdhfoiuncxk.db'

    tableNameList = ItemNameList

    password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName

    dataBasePath = Database

    iDValue = 0
    colname = 'Col0'

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)


    for i in range(len(tableNameList)):
        # print(tableNameList[i])

        datatype = 'TEXT'

        colList = [[colname , datatype]]

        # print(colName[i])

        # print(colList)
        # TableCreated = False
        try:
            obj.createTable(tableName = tableNameList[i] , colList = colList , makeSecure=True , commit=True)

            # print('table created now')
        except Exception as e:
            if str(e) == 'table name already exist in data base':
                # print('Table already created')
                pass
            else:
                print(e)


        try:
            obj.deleteDataInTable(tableNameList[i] , iDValue , commit = True , raiseError = True , updateId = True)
        except Exception as e:
            if str(e) == 'ID = 0 not found while deletion process':
                # print('ID does not exist')
                pass


        colList = [colValueList[i], datatype]

        obj.insertIntoTable(tableName=tableNameList[i] , insertList=colList , commit = True)

        # TableData2 = obj.getDataFromTable(tableNameList[i] , raiseConversionError = True , omitID = False)
        
        # print(tableNameList[i])
        # print(TableData2)
        
        
        
        obj.updateInTable(tableNameList[i] , iDValue , colName=colname , colValue = colValueList[i] , commit = True , raiseError = True)


        # TableData2 = obj.getDataFromTable(tableNameList[i] , raiseConversionError = True , omitID = False)
        # # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        print('Done')




def WriteTableSecuredDictionary(InputDictionary):


    # Database = 'fhjlasjdhfoiuncxk.db'


    ItemNameList = InputDictionary.keys()
    
    
    colValueList = InputDictionary.values()


    WriteTableSecuredList(ItemNameList,colValueList)

    





def WriteTableSecuredIten(ItemName,ItenValue):


    Database = 'fhjlasjdhfoiuncxk.db'

    password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'


    dataBasePath = Database

    iDValue = 0
    colname = 'Col0'

    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)


    datatype = 'TEXT'

    colList = [[colname , datatype]]

    try:
        obj.createTable(tableName = ItemName , colList = colList , makeSecure=True , commit=True)

        # print('table created now')
    except Exception as e:
        if str(e) == 'table name already exist in data base':
            # print('Table already created')
            pass
        else:
            print(e)


    try:
        obj.deleteDataInTable(ItemName, iDValue , commit = True , raiseError = True , updateId = True)
    except Exception as e:
        if str(e) == 'ID = 0 not found while deletion process':
            # print('ID does not exist')
            pass


    # colList = [ItemName, datatype]

    obj.insertIntoTable(tableName=ItemName , insertList=colList , commit = True)

  
    obj.updateInTable(ItemName , iDValue , colName=colname , colValue = ItenValue , commit = True , raiseError = True)


    print('Done')



def GetAllTableSecuredData():

    Database = 'fhjlasjdhfoiuncxk.db'


    # tableNameList = ItemNameList

    password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName


    dataBasePath = Database


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)

    # print(obj.getAllTableNames()[2][0])

    Itens = obj.getAllTableNames()

    # print(Itens)

    # print(tableNameList)

    ItemNameList = []
    OuptputList = []
    for i in range(len(Itens)-2):

        ItenToAppend = Itens[i+2][0]
        TableData2 = obj.getDataFromTable(ItenToAppend, raiseConversionError = True , omitID = True)
        # print(TableData2)
        
        ItemNameList.append(ItenToAppend)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])
        OutputValueToAppend = TableData2[1][0][0]

        OuptputList.append(OutputValueToAppend)

    return [OuptputList], ItemNameList





def GetAllTableDictionarySecuredData():

    # Database = 'fhjlasjdhfoiuncxk.db'

    Datalist, names = GetAllTableSecuredData()

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        print(e)

    return dictValue

    



def GetTableItensListSecuredData(ItemNameList):

    Database = 'fhjlasjdhfoiuncxk.db'

    tableNameList = ItemNameList

    password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName


    dataBasePath = Database


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)

    # print(obj.getAllTableNames()[2][0])

    # Itens = obj.getAllTableNames()

    # print(tableNameList)

    OuptputList = []
    for i in range(len(tableNameList)):

        TableData2 = obj.getDataFromTable(tableNameList[i], raiseConversionError = True , omitID = True)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

        OuptputList.append(TableData2[1][0][0])

    return [OuptputList], ItemNameList





def GetTableItensDictionarySecuredData(ItemNameList):

    # Database = 'fhjlasjdhfoiuncxk.db'

    Datalist, names = GetTableItensListSecuredData(ItemNameList)

    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        print(e)

    return dictValue




def GetTableSingleItensSecuredData(ItemName):


    Database = 'fhjlasjdhfoiuncxk.db'


    tableNameList = ItemName

    password = ';alkdfj9ine93mnksdo03md090u0s03mklsmflslkdkjfsldk'

    # DbLocation = ''
    # DbName = "pysqlitecipher.db"

    # dataBasePath = DbLocation + DbName


    dataBasePath = Database


    obj = sqlitewrapper.SqliteCipher(dataBasePath = dataBasePath , checkSameThread = False , password = password)

    # print(obj.getAllTableNames()[2][0])

    # Itens = obj.getAllTableNames()

    print(tableNameList)

    # OuptputList = []
    # for i in range(len(tableNameList)):

    TableData2 = obj.getDataFromTable(ItemName, raiseConversionError = True , omitID = True)
        # print(TableData2)

        # print(tableNameList[i])
        # print(TableData2)

        # print(TableData2[1][0][0])

        # OuptputList.append(TableData2[1][0][0])
    OutputIten = str(TableData2[1][0][0])

    return OutputIten


def DeleteDb():

    currentWorkingDirectory = os.getcwd()

    Database = 'fhjlasjdhfoiuncxk.db'

    fileLocation = currentWorkingDirectory + Database

    os.remove(fileLocation)
        

# Database = "pysqlitecipher.db"


# ItemNameList = ['Item1', 'Item2', 'Item3']       # item to add

# ItemNameList = ['Item2', 'Item1']       # item to add
# colValueList = [['NewValue1', 'NewValue2', 'NewValue3'],['NewValue1', 'NewValue2', 'NewValue3']]    # item value

# WriteTableSecuredList(ItemNameList,colValueList)



# print(GetTableItensListSecuredData(ItemNameList))

# print(GetTableItensDictionarySecuredData(ItemNameList))


# print(GetAllTableSecuredData())

# print(GetAllTableDictionarySecuredData())

# ItemName = 'Item2'

# print(GetTableSingleItensSecuredData(ItemName))

# ItemName = 'Item5'
# ItenValue = 'Item5ValueTT'

# WriteTableSecuredIten(ItemName,ItenValue)


print(GetAllTableSecuredData())