import getTableData


Database='MercadoLivreItemData.db'

TableName='ItemsData'


dataNameList = ['NumeroDeItensVendidos','NomeDoItem','ItemPrice', 'ItemSiteLocation','RequestTime']





Items = getTableData.GetTableData(Database=Database,TableName=TableName,ErrorIfNotFound=False,willChangeDirectory=False)

print(Items)


# Tables = getTableData.getTables(Database=Database,willChangeDirectory=False)

# print(Tables)