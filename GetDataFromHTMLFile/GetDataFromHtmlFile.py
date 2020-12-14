# importing the libraries
from bs4 import BeautifulSoup
import html5lib
import os

import pprint

from lxml import html



def tableDataText(table):       
    rows = []
    trs = table.find_all('tr')
    headerow = [td.get_text(strip=True) for td in trs[0].find_all('th')] # header row
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append([td.get_text(strip=True) for td in tr.find_all('td')]) # data row
    return rows

def removeUnwantedChars(Table):
    finalTable=[]

    tabley= len(Table)
    tablex=len(Table[0])

    # print('tablex: ',tablex)

    # print('tabley:',tabley)
    # for row in range(tablex):
    
    for row in range(len(Table)):

        remove1='R$\xa0'
        remove2='.'
        remove3='R$ '
        replace1=','
        # finalTable.append([])

        # print(finalTable)

        # print(Table[row])

        # finalTable.append(Table[row])
        finalTable1=[]
        for itemId in range(len(Table[row])):
            # print(Table[row][itemId])
            # Table[row][itemId]
            # print('itemId: ',itemId)

            # print('row: ',row)

            value = Table[row][itemId]

            # x = txt.replace("bananas", "apples")

            # value1=value.replace(remove1, "")

            # value2=value1.replace(remove2, "")

            # value3=value2.replace(replace1, remove2)

            # print(value)

            value=value.replace(remove1, "")

            # value2=list(value)

           


            value=value.replace(remove2, "")

            # value=value.replace(remove3, "")

            

            

            value=value.replace(replace1, remove2)

            # print(finalTable)

            # print(value)

            # print(value3)

            # Table[row][itemId]=value

            finalTable1.append(value)

            # Table[row][itemId]=value3

        # print(finalTable1)

        finalTable.append(finalTable1)

    return finalTable

def getColumnListFromTableList(Table, columnNumber):

    ColumnAsked=[]
    for row in range(1, len(Table)):
        for column in range(len(Table[columnNumber])):
            if column == columnNumber:
                value=Table[row][columnNumber]
                
                ColumnAsked.append(float(value))
        
    return ColumnAsked

def sumAllList(List):

    BListItem = 0

    for i in range(len(List)):
        List2 = List[i] + BListItem
        BListItem = List2

    return List2
        
        


            


       

    




url="Simulation105.htm"

# url="Simulation420.htm"


cwdUsed=os.getcwd()

# print(cwdUsed+'\\')

Filelofcation=cwdUsed+'\\'+ url

html_content=open(Filelofcation,'r' , encoding='UTF-8')

soup = BeautifulSoup(html_content, "html5lib")
# print(soup.prettify()) # print the parsed data of html


data = {}
#Get the table having the class wikitable
gdp_table = soup.find("table", attrs={"class": "MuiTable-root"})

# print(gdp_table.prettify())


list_table = tableDataText(gdp_table)

# print(list_table)

# print(list_table[0][3])



list_table2 = removeUnwantedChars(Table=list_table)

# print(list_table2)

pprint.pprint(list_table2)

columnNumber=2

AskedColumn=getColumnListFromTableList(Table=list_table2, columnNumber= columnNumber)

print(AskedColumn)

SumList = sumAllList(List=AskedColumn)

MaxValueEmp=SumList*12

print("ValorMaximoPeloEmprestimo ",MaxValueEmp)


if url=="Simulation420.htm":

    NumeroDeMesesPagosUmaVez=3


    print('NumeroDeMesesPagosUmaVez: ',NumeroDeMesesPagosUmaVez)

    Divisor=12/NumeroDeMesesPagosUmaVez

    print('Divisor: ',Divisor)

    RealPaidValue=MaxValueEmp/Divisor

    print('RealPaidValue: ',RealPaidValue)







# gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 

# # print(gdp_table_data)


# # print(gdp_table_data[0])

# tabledata0=gdp_table_data[0].find_all("td", attrs={"class": "MuiTableCell-root MuiTableCell-body MuiTableCell-alignCenter"})

# print(tabledata0)



# print(len(gdp_table_data))

# print(len(gdp_table_data[0]))

# tabley=len(gdp_table_data)

# tablex=len(gdp_table_data[0])

# print(tabley)

# print(tablex)

# print(gdp_table_data[0][0])

# headings = []
# for td in gdp_table_data[0].find_all("td"):
#     # remove any newlines and extra spaces from left and right
#     headings.append(td.b.text.replace('\n', ' ').strip())

# print(headings)


# # print(gdp_table_data)

# headings = []
# for td in gdp_table_data[0].find_all("td"):
#     # remove any newlines and extra spaces from left and right
#     headings.append(td.b.text.replace('\n', ' ').strip())

# # Get all the 3 tables contained in "gdp_table"
# for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
#     # Get headers of table i.e., Rank, Country, GDP.
#     t_headers = []
#     for th in table.find_all("th"):
#         # remove any newlines and extra spaces from left and right
#         t_headers.append(th.text.replace('\n', ' ').strip())
    
#     # Get all the rows of table
#     table_data = []
#     for tr in table.tbody.find_all("tr"): # find all tr's from table's tbody
#         t_row = {}
#         # Each table row is stored in the form of
#         # t_row = {'Rank': '', 'Country/Territory': '', 'GDP(US$million)': ''}

#         # find all td's(3) in tr and zip it with t_header
#         for td, th in zip(tr.find_all("td"), t_headers): 
#             t_row[th] = td.text.replace('\n', '').strip()
#         table_data.append(t_row)

#     # Put the data for the table with his heading.
#     data[heading] = table_data

# print(data)

