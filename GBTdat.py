import yfinance

import base93Characterconversion



fileName = "adfasdgaf.rvx"

def WriteFl(fileName):

    data = yfinance.download(tickers='BTC-USD', period = '5h', interval = '1m',progress=False)

    dataString = ''
    for i in range(len(data)):
        dataString = dataString + str(list(data.iloc[i][:-1])).replace('[','').replace(']','').replace(' ','').replace('.','').replace(',', '')
        
    file1 = open(fileName,"w")

    file1.write(dataString)

    file1.close() 



def GetFlInf(fileName):

    file1 = open(fileName,"r+") 
  
    dataString = file1.read()

    checkLocation = dataString[2145:2149]

    SnGten = dataString[int(checkLocation):int(checkLocation) + 58]

    TimeBased = False

    OtherNumer = SnGten

    TableDataValueSS2 = base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)

    checkLocation = dataString[5897:5901]

    SnGten = dataString[int(checkLocation):int(checkLocation) + 25]

    TimeBased = False

    OtherNumer = SnGten

    TableDataValueSS3 = str(base93Characterconversion.base93Characterconversion(TimeBased=TimeBased, OtherNumer=OtherNumer)) + '.db'


    return TableDataValueSS3, TableDataValueSS2

        


# WriteFl(fileName)

# print(GetFlInf(fileName))