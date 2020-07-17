import sqlite3

import changeDirectory

def DropSqlTable(Database, TableName):

    changeDirectory.ChangeTokey()

    conn  = sqlite3.connect(Database)

    c      = conn.cursor()

    dropTableStatement = "DROP TABLE "+TableName

    try:
        c.execute(dropTableStatement)
        print("Table Dropped Sucessfully")
    except Exception as e:
        print(e)

    c.close() 
    conn.close() 

def DropTable(TableName="qqqqqqqrrrrrrSetValuesrrrrrrqqqqqqq"):

    TableName=TableName
    Database="AutoFormFiller.db"

    DropSqlTable(Database=Database, TableName=TableName)


# DropTable()