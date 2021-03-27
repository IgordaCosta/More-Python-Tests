import sqlite3 

import changeDirectory
 
  
def create_table(Database,ColumnsList,TableName,TypeList=[]): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    if TypeList==[]:
        string=" ( id integer PRIMARY KEY,"
        for i in range(len(ColumnsList)):
            print(i)
            print(string)
            print(ColumnsList[i])
            string=string+ColumnsList[i] +" TEXT, "
            print(string)
        string = string[:-2]
        string=string+")"

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableName+string) 
        print('CREATE TABLE IF NOT EXISTS '+ TableName+string) 

    else:
        string=" ( id integer PRIMARY KEY,"
        for i in range(len(ColumnsList)):
            print(i)
            string=string+ColumnsList[i] +" "+ TypeList[i] +", "
            print(string)
        string = string[:-2]
        string=string+")"

        c.execute('CREATE TABLE IF NOT EXISTS '+ TableName+string) 
        print('CREATE TABLE IF NOT EXISTS '+ TableName+string) 

  
def data_entry(Database,TableName,ColumnsList,ValuesList): 
    conn = sqlite3.connect(Database) 
    c = conn.cursor() 

    ColumnsList=list(ColumnsList)

    ValuesList=list(ValuesList)
    
    string1=" ( "
    string2=" VALUES ( "
    for i in range(len(ColumnsList)):
        print(i)


        ColumnsList[i] = ColumnsList[i].replace("'", '"')

        ValuesList[i] = ValuesList[i].replace("'", '"')



        string1=string1+str(ColumnsList[i]) +", "

        string2=string2+"'"+str(ValuesList[i])+"'"+", "
        print(string1)
        print(string2)
    string1 = string1[:-2]
    string1=string1+")"

    string2 = string2[:-2]
    string2=string2+")"

    commandMade="INSERT INTO "+TableName+string1+string2
    print(commandMade)
    c.execute(commandMade) 
    conn.commit() 
  

def CreateTableAndInsertValues(Database,TableName,TypeList ,ColumnsList=[],ValuesList=[],Dictionary={},changeTheDirectory = True):
    # conn = sqlite3.connect('pythonDB.db') 
    if changeTheDirectory:
        changeDirectory.ChangeTokey()

    conn = sqlite3.connect(Database) 
    c = conn.cursor() 


    if Dictionary!={}:

        ColumnsList, ValuesList = zip(*Dictionary.items())


    create_table(Database=Database,ColumnsList=ColumnsList, TableName=TableName,TypeList=TypeList)
    data_entry(Database=Database,TableName=TableName,ColumnsList=ColumnsList, ValuesList=ValuesList)
    print("Done database write")
    c.close() 
    conn.close() 


def SetValues(TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq",Database="AutoFormFiller.db",ColumnsList=[],ValuesList=[],Dictionary={}, changeTheDirectory = True):

    if Dictionary!={}:

        ColumnsList, ValuesList = zip(*Dictionary.items())


    if ColumnsList!=[]:
        TypeList=[]
        TableName=TableName
        Database = Database

        for i in range(len(ColumnsList)):
            TypeList.append("text")

        CreateTableAndInsertValues(Database=Database,TableName=TableName,ColumnsList=ColumnsList,ValuesList=ValuesList,TypeList=TypeList,changeTheDirectory = changeTheDirectory)




# Dictionary={'col1': 'val1', 'col2': 'val2', 'col3': 'val3', 'col4': 'val4', 'col5': 'val5'}

# # ColumnsList=["col1","col2","col3","col4","col5"]
# # ValuesList=["val1","val2","val3","val4","val5"]

# # SetValues(ColumnsList=ColumnsList,ValuesList=ValuesList)


# SetValues(Dictionary=Dictionary)