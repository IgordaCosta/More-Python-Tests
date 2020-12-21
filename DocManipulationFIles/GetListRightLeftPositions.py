import FindNumberWordInString


def GetListRightLeftPositions(word, stringUsed):

    # RightLeftList= []
    
    wordRight= word + " "

    NumWord = FindNumberWordInString.FindNumberWordInString(word=wordRight , stringUsed=stringUsed)

    ListOfWordPositionsRight=[]

    for i in range(NumWord):

        LocationOfWord = stringUsed.find(wordRight) 

        ListOfWordPositionsRight.append(LocationOfWord)

        stringUsed = stringUsed.replace(wordRight,"",1)

        # print(stringUsed)


    # print(ListOfWordPositionsRight)

    # print(stringUsed)

    # RightLeftList.append(ListOfWordPositionsRight)

    wordLeft= " "+word

    NumWord = FindNumberWordInString.FindNumberWordInString(word=wordLeft , stringUsed=stringUsed)

    ListOfWordPositionsLeft=[]

    for i in range(NumWord):

        LocationOfWord = stringUsed.find(wordLeft) 

        ListOfWordPositionsLeft.append(LocationOfWord)

        stringUsed = stringUsed.replace(wordLeft,"",1)

        # print(stringUsed)


    # print(ListOfWordPositionsLeft)

    # print(stringUsed)


    # RightLeftList.append(ListOfWordPositionsLeft)

    # print(RightLeftList)


    return ListOfWordPositionsRight, ListOfWordPositionsLeft









word ='dog'


stringUsed = "dog cat meau dog kitty dog"



ListOfWordPositionsRight, ListOfWordPositionsLeft = GetListRightLeftPositions(word, stringUsed)


print('ListOfWordPositionsRight: ' ,ListOfWordPositionsRight )

print('ListOfWordPositionsLeft: ', ListOfWordPositionsLeft)





