import sqlite3
import os

import changeDirectory

import dropSqlTable

import createSqliteTableFromList


def GetAllTableNamesFromDatabase(Database,willChangeDirectory=True):
    if willChangeDirectory:
        changeDirectory.ChangeTokey()


    Exists=os.path.isfile(Database)

    if Exists:
        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        c.execute("SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'") 
        conn.commit() 

        rows = c.fetchall()

        TableList=[]
        for row in rows:
            value=list(row)[0]
            print(value)
            TableList.append(value)

        print(TableList)
        print("Done Database Read")

        c.close() 
        conn.close()

        return TableList

    else:
        print("could not find file!")

def GetTableDataFromTable(Database="AutoFormFiller.db",TableName='',TableNumber='',ErrorIfNotFound=True, willChangeDirectory=True):
    if willChangeDirectory:
        changeDirectory.ChangeTokey()
    

    if TableNumber !='':
        TableList=GetAllTableNamesFromDatabase(Database,willChangeDirectory=willChangeDirectory)
        TableName=TableList[TableNumber]
        print(TableName,"TableName used")
    
    if TableName !='':
        Datalist, names= '',''

        conn = sqlite3.connect(Database) 
        c = conn.cursor() 

        try:
            c.execute("SELECT * FROM "+ TableName)

            names = [description[0] for description in c.description]

            rows = c.fetchall()

            Datalist=[]
            for row in rows:
                # print(row)
                Datalist.append(list(row))

            # print(Datalist)

            # print(Datalist[0][4])

            # print('Datalist')

            # print(names)

            # print("names")

        except Exception as e:
            print(e)

        c.close() 
        conn.close() 

        if Datalist=='' and ErrorIfNotFound:
            raise Exception("The variable was not found!")


        return Datalist, names


def getTables(Database="AutoFormFiller.db",willChangeDirectory=True):

    # Database="AutoFormFiller.db"

    GetAllTableNamesFromDatabase(Database,willChangeDirectory=willChangeDirectory)


def GetTableData(Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):

    # TableName=TableName
    # Database="AutoFormFiller.db"

    dictValue = {}

    Datalist, names=GetTableDataFromTable(Database=Database,TableName=TableName,ErrorIfNotFound=ErrorIfNotFound,willChangeDirectory=willChangeDirectory)
    
    try: 
        Datalist=Datalist[0]

        dictValue = dict(zip(names, Datalist))
    
    except Exception as e:
        print(e)

    return dictValue

def GetDataFromDatabase(dataName,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):
    dictValue=GetTableData(Database=Database,TableName=TableName,ErrorIfNotFound=ErrorIfNotFound,willChangeDirectory=willChangeDirectory)

    data=dictValue[dataName]

    return data

def GetMultipleDataFromDatabase(dataNameList,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):
    dictValue=GetTableData(Database=Database,TableName=TableName,ErrorIfNotFound=ErrorIfNotFound,willChangeDirectory=willChangeDirectory)

    Dictionary={}
    for i in range(len(dataNameList)):
        data=dictValue[dataNameList[i]]
        Dictionary[dataNameList[i]]=data


    return Dictionary

def WriteDataDatabase(data,dataName,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',willChangeDirectory=True):
    Dictionary=GetTableData(ErrorIfNotFound=False,Database=Database,TableName=TableName,willChangeDirectory=willChangeDirectory)
    Dictionary[dataName]=data

    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)



def MultipleListWriteDataDatabase(dataList,dataNameList,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):
    Dictionary=GetTableData(ErrorIfNotFound=False,Database=Database,TableName=TableName,willChangeDirectory=willChangeDirectory)
    for i in range(len(dataNameList)):
        Dictionary[dataNameList[i]]=dataList[i]

    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)


def MultipleDictionaryWriteDataDatabase(DictionaryAdd,Database="AutoFormFiller.db",TableName='qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq',ErrorIfNotFound=True,willChangeDirectory=True):
    Dictionary0=GetTableData(ErrorIfNotFound=False,Database=Database,TableName=TableName,willChangeDirectory=willChangeDirectory)

    Dictionary = dict(list(Dictionary0.items()) + list(DictionaryAdd.items()))

    print(Dictionary)
    
    try:
        del Dictionary['id']
    except:
        pass

    dropSqlTable.DropTable()

    createSqliteTableFromList.SetValues(Dictionary=Dictionary)



# # getTables()

# getTables(Database="AutoFormFiller.db",willChangeDirectory=True)

# # GetTableDataFromTable(Database="AutoFormFiller.db",TableName='KEY_file1',TableNumber='')

# # data=50
# # dataName="firstData"

# # WriteDataDatabase(data,dataName)

# dictValue=GetTableData(Database="AutoFormFiller.db",TableName='FontAndItsSize',ErrorIfNotFound=True,willChangeDirectory=True)
# import pprint

# dictValue=GetTableData(Database="AutoFormFiller.db",ErrorIfNotFound=True,willChangeDirectory=True)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(dictValue)

# print('LocationToAddFileOnApp :',str(dictValue['LocationToAddFileOnApp']))


# print(dictValue["File Saved Location"])

# data='abc'

# dataName='rw'

# WriteDataDatabase(data,dataName)

# dataframe=dictValue["dataframe"]
# try:
#     dataframe=dictValue["datfdgsdgfaframe"]
# except KeyError:
#     print("the value doese not exist")

# print("it continued")

# print(dataframe)

# # dropSqlTable.DropTable()
# # dictValue=GetTableData()


# # print("bellow is the data1")

# # print(dictValue)



# DictionaryAdd={'Data100': '11','Data200': '22','Data300': '33'}

# MultipleDictionaryWriteDataDatabase(DictionaryAdd)


# dictValue=GetTableData()


# print("bellow is the data2")

# print(dictValue)

# # fname=dictValue['fname']

# # filePath=dictValue['filePath']

# # fileNameOnly=dictValue['fileNameOnly']



# # col1=dictValue['col1']

# # print(col1)





