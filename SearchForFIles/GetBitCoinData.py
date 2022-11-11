import pandas
import yfinance

import base93Characterconversion






data = yfinance.download(tickers='BTC-USD', period = '22h', interval = '15m')

TableData = pandas.DataFrame(data)

TableDataValue = TableData.index[0]

print(TableDataValue)

TableDataValueSS = str(TableDataValue).replace('-','d').replace(' ', 't').replace(':','r')

print(TableDataValueSS)

OtherNumer= TableDataValueSS

TableDataValueSS2 = base93Characterconversion.base93Characterconversion(OtherNumer=OtherNumer)

print(TableDataValueSS2)




