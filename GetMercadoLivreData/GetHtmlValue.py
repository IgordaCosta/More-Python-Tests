try:
    # Python 2
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from bs4 import BeautifulSoup
from datetime import datetime





def GetHtmlValue(url, CssSelector):
    response = urlopen(url)

    soup = BeautifulSoup(response)

    resultSelect = soup.select(CssSelector)
    
    resultSelectText = resultSelect[0].text
    
    return resultSelectText 


def GetHtmlValueFromList(url, CssSelectorList):
    response = urlopen(url)

    soup = BeautifulSoup(response)
    
    resultSelectTextList = []
    
    for CssSelector in CssSelectorList:

        resultSelect = soup.select(CssSelector)

        resultSelectText = resultSelect[0].text
        
        resultSelectTextList.append(resultSelectText)
        
    
    return resultSelectTextList 


def GetTextParagraphAsList(Location, SubLocation, fileName):

    fullLocation = Location + SubLocation + fileName

    file1 = open(fullLocation,"r+")

    LocationList = file1.readlines()

    file1.close()
    
    return LocationList



def DoubleListSitesInformation(LocationList, CssSelectorList):
    
    timeNow0 = datetime.now() 
    timeNow = timeNow0.strftime('%Y/%m/%d-%H:%M_H') 

    SiteValuesList = []
    for item in LocationList:

#         CssSelectorList = ['.ui-pdp-subtitle', '.ui-pdp-title', 'span.price-tag-fraction:nth-child(3)' ]

        resultGotten = GetHtmlValueFromList(item, CssSelectorList)

        resultGotten[0] = resultGotten[0][9:-9]

        resultGotten.append(item)

        resultGotten.append(timeNow)

        SiteValuesList.append(resultGotten)

    return SiteValuesList