import selenium      # Using Chrome to access web
import time
from selenium import webdriver


import WriteListToTextFile

import GetTextItemsFromList



cromeDriverPath = r"C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(executable_path=cromeDriverPath)      # Open the website


site = "https://translate.google.com/?hl=pt-PT"
driver.get(site)






# pathUsed = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'

pathUsed = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea'


pathUsed3 = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span/span'

pathUsed2 = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div[1]/div[1]/span[1]'

pathUsed4 = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span'
# ListOInputText = ['New data', 'Movie is good', 'Ok it is done' ]

textFileLocation = r'C:\Users\Tigereye\Downloads\bad-girls-2021-english-yify-386674' + '\\'

textFileName = 'MovieSubtilteTest.srt'

textFileName2 = 'MovieSubtilteTestOutput2222.srt'

ListOInputText = GetTextItemsFromList.GetTextItemsFromList(textFileLocation=textFileLocation,textFileName=textFileName)

ListOfTranslatedText = []
GottenText0 = ''

TextToSend2 = ''

print(ListOInputText)

IntValue = ''

IntValue2 = ''



for TextToSend in ListOInputText:
    
    # print(TextToSend)

    # print(type(TextToSend))
        
    ToTranslateText = driver.find_elements_by_xpath(pathUsed)[0]

    print(ToTranslateText)

    # driver.find_element(By.xpath = )

    ToTranslateText.clear()


    ToTranslateText.send_keys(TextToSend)






NotDone = True
while NotDone:

    

    try:
        GottenText = driver.find_elements_by_xpath(pathUsed2)[0].text

        # print(GottenText)

        # print('GottenText above')

        GottenTextAdd = GottenText.replace('\n', '') 

        # print(GottenTextAdd)

        # print('GottenTextAdd above')

        if GottenText0 == GottenTextAdd:
            time.sleep(1)
        elif 'Tradução' == GottenText:
            time.sleep(1)
        elif 'A traduzir...' == GottenText:
            time.sleep(1)
        else:
            GottenText0 = GottenTextAdd
            NotDone = False
    except:
        pass

    if NotDone:
        try:
            # pathUsed3 = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div[1]/div[1]/span[1]'
            
            # print( driver.find_elements_by_xpath(pathUsed3)[0])
            GottenText = driver.find_elements_by_xpath(pathUsed3)[0].text


            # print(GottenText)

            # print('GottenText above2')

            replaceText = '''
'''

            GottenTextAdd = GottenText.replace(replaceText, ' ') 

            # print(GottenTextAdd)

            # print('GottenTextAdd above2')




            if GottenText0 == GottenTextAdd:

                if IntValue2 == IntValue:
                    time.sleep(1)
                else:

                    ottenText0 = GottenTextAdd

                    GottenText00 = GottenText
                    NotDone = False

                    IntValue2 = IntValue
            if GottenText00 == GottenText:

                if IntValue2 == IntValue:
                    time.sleep(1)
                else:

                    ottenText0 = GottenTextAdd

                    GottenText00 = GottenText
                    NotDone = False

                    IntValue2 = IntValue

            elif 'Tradução' == GottenText:
                time.sleep(1)
            elif 'A traduzir...' == GottenText:
                time.sleep(1)
            else:
                GottenText0 = GottenTextAdd

                GottenText00 = GottenText
                NotDone = False

                IntValue2 = IntValue
        except:
        
            pass

    if NotDone:
        try:
            # pathUsed3 = '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div[1]/div[1]/span[1]'
            
            # print( driver.find_elements_by_xpath(pathUsed3)[0])
            GottenText = driver.find_elements_by_xpath(pathUsed4)[0].text


            # print(GottenText)

            # print('GottenText above2')

            replaceText = '''
'''

            GottenTextAdd = GottenText.replace(replaceText, ' ') 

            # print(GottenTextAdd)

            # print('GottenTextAdd above2')




            if GottenText0 == GottenTextAdd:

                if IntValue2 == IntValue:
                    time.sleep(1)
                else:

                    ottenText0 = GottenTextAdd

                    GottenText00 = GottenText
                    NotDone = False

                    IntValue2 = IntValue

            if GottenText00 == GottenText:
                
                if IntValue2 == IntValue:
                    time.sleep(1)
                else:

                    ottenText0 = GottenTextAdd

                    GottenText00 = GottenText
                    NotDone = False

                    IntValue2 = IntValue

            elif 'Tradução' == GottenText:
                time.sleep(1)
            elif 'A traduzir...' == GottenText:
                time.sleep(1)
            else:
                GottenText0 = GottenTextAdd

                GottenText00 = GottenText
                NotDone = False

                IntValue2 = IntValue
        except:
        
            time.sleep(1)


    



        # print(GottenText)

        # print(GottenTextAdd)

        ListOfTranslatedText.append(GottenTextAdd)








print(ListOfTranslatedText)
print('GottenText above')

ListToWrite = ListOfTranslatedText


WriteListToTextFile.WriteListToTextFile(textFileLocation=textFileLocation,textFileName=textFileName2, ListToWrite= ListToWrite)