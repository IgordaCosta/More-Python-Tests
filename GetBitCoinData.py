import pandas
import yfinance
import random

import base93Characterconversion



def GetDbNameFromTime(TimeUsed = ''):

    if TimeUsed == '':
        data = yfinance.download(tickers='BTC-USD', period = '5d', interval = '1m',progress=False)

        TableData = pandas.DataFrame(data)

        TableDataValue = TableData.index[-1]

        # print(TableDataValue)

        TableDataValueSS = str(TableDataValue).replace('-','').replace(' ', '').replace(':','')

        # print(TableDataValueSS)

        OtherNumer= TableDataValueSS
    else:
        # OtherNumer= TimeUsed
        try:
            OtherNumer = int(TimeUsed)
            TimeChange = str(OtherNumer)
            TableDataValue = TimeChange[:4] + '-' + TimeChange[4:6] +  '-' + TimeChange[6:8] +  ' ' + TimeChange[8:10] +  ':' + TimeChange[10:12] +  ':' +TimeChange[12:14]

        except:
            TableDataValue = TimeUsed
            OtherNumer = str(TableDataValue).replace('-','').replace(' ', '').replace(':','')
            

        # TableDataValue = OtherNumer

    TimeBased = False

    TableDataValueSS2 = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer) + '.db'

    # print(TableDataValueSS2)


    return TableDataValueSS2 , TableDataValue




def GetDbSn(DateToCheck):
    # print(GetDbNameFromTime(TimeUsed='20221107203200'))


    data = yfinance.download(tickers='BTC-USD', period = '5d', interval = '1m',progress=False)

    # print(data)

    DataFromDF = pandas.DataFrame(data)

    # DateToCheck= '2022-11-07 22:39:00'

    # ColumnList = ['Open','High','Low','Close', 'Adj Close']

    ColumnList = DataFromDF.columns

    # LenColumnList = len(DataFromDF.columns)


    StringColumnSum = ''
    for i in range(len(ColumnList)-1):
        j = i
        # print(j)
        StringColumnSum = StringColumnSum + str((int(DataFromDF[ColumnList[j]][DateToCheck]*1000000000)))

    # print(StringColumnSum)


    TimeBased = False

    OtherNumer = StringColumnSum

    TableDataValueSS2 = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)
    
    
    return TableDataValueSS2





data = yfinance.download(tickers='BTC-USD', period = '5h', interval = '1m',progress=False)

# print(data)



fileName = "adfasdgaf.rvx"

def WriteFl(fileName):

    dataString = ''
    for i in range(len(data)):
        dataString = dataString + str(list(data.iloc[i][:-1])).replace('[','').replace(']','').replace(' ','').replace('.','').replace(',', '')
        


    file1 = open(fileName,"w")

    
    # \n is placed to indicate EOL (End of Line)
    file1.write(dataString)

    file1.close() #to change file access modes
    


def GetFlInf(fileName):


    file1 = open(fileName,"r+") 
  

    dataString = file1.read()


    # print(len(dataString))


    checkLocation = dataString[2145:2149]

    # print(checkLocation)


    SnGten = dataString[int(checkLocation):int(checkLocation) + 58]

    # print(SnGten)

    TimeBased = False

    OtherNumer = SnGten


    TableDataValueSS2 = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)

    # print(TableDataValueSS2)

    # print(len(TableDataValueSS2))

        








    checkLocation = dataString[5897:5901]

    # print(checkLocation)


    SnGten = dataString[int(checkLocation):int(checkLocation) + 25]

    # print(SnGten)

    TimeBased = False

    OtherNumer = SnGten


    TableDataValueSS3 = str(base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)) + '.db'

    # print(TableDataValueSS3)

    # print(len(TableDataValueSS3))

    return TableDataValueSS3, TableDataValueSS2

        


WriteFl(fileName)

print(GetFlInf(fileName))