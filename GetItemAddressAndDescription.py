import readSqlDatabase
import ChangeStartupDirectoryT
import getTableData




def GetItemAddressAndDescription():

    
    Folder="AutoFormFillerKey"

    ChangeStartupDirectoryT.ChangeStartupDirectory(Folder=Folder)


    # datafillName="file1"


    TableGotten=getTableData.GetTableData()


    datafillName=TableGotten['datafillName']

    print(datafillName)


    databaseUsed0 = readSqlDatabase.readSqlDatabase(table_name="KEY_"+datafillName)
    databaseUsed=databaseUsed0[0]

    # print(databaseUsed)

    itemAddress=databaseUsed.columns.values[1:]

    itemDescription=databaseUsed.values[0][1:]

    print(itemAddress)

    print(itemDescription)



GetItemAddressAndDescription()