


def RemoveMultipleSpacesInString(inputText):
    Text2 = inputText.split(' ')

    Text2List = [ item for item in Text2 if item != '']

    outputText = ' '.join(Text2List)

    return outputText
    

# inputText = 'This      is a great and   big bird'

# print(RemoveMultipleSpacesInString(inputText))