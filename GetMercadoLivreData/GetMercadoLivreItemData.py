import pprint
import GetHtmlValue
import getTableData
import createSqliteTableFromList


CssSelectorList = ['.ui-pdp-subtitle', '.ui-pdp-title', 'span.price-tag-fraction:nth-child(3)' ]

Location = r'C:\Users\IgorDC\Desktop\MercadoLivreLocations' + '\\'

SubLocation = 'drone' + '\\'

fileName= 'SiteLocations.txt'

dataNameList = ['NumeroDeItensVendidos','NomeDoItem','ItemPrice', 'ItemSiteLocation','RequestTime']

TableName = 'ItemsData'

Database = 'MercadoLivreItemData.db'


LocationList = GetHtmlValue.GetTextParagraphAsList(Location, SubLocation, fileName)

# print(LocationList)


SiteValuesList =GetHtmlValue.DoubleListSitesInformation(LocationList, CssSelectorList)

pprint.pprint(SiteValuesList)




# for SiteItemInfo in range(len(SiteValuesList)):
#     print(SiteItemInfo)
#     if SiteItemInfo == 0:
#         createSqliteTableFromList.SetValues(TableName=TableName,Database=Database,ColumnsList=dataNameList,ValuesList=SiteValuesList[SiteItemInfo],Dictionary={}, changeTheDirectory = False)
    
# print('Done')


