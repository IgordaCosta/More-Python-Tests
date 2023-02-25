


def RemoveMultipleSpacesInString(inputText):
    Text2 = inputText.split(' ')

    Text2List = [ item for item in Text2 if item != '']

    outputText = ' '.join(Text2List)

    return outputText
    



def RemoveSpacesAndKeepItems(inputText, textToKeepList):

    inputText2 = RemoveMultipleSpacesInString(inputText)

    # print(inputText2)

    for textToKeep in textToKeepList:
        
        inputText2List = inputText2.split(textToKeep)

        # print(inputText2List)

        inputText3 = ''
        for item in inputText2List:
            if item != '':
                if item == '\n':
                    item= item.replace('\n', textToKeep.strip()+ '\n')
                else:
                    item = item.strip()
                              
            else:
                item= item.replace('', textToKeep)


            inputText3 = inputText3 + item

        inputText2 = inputText3


    return inputText2



# inputText = '< This      is a great and   big bird >'

# textToKeepList = [ '<', '>']

# print( RemoveSpacesAndKeepItems(inputText, textToKeepList) )



    