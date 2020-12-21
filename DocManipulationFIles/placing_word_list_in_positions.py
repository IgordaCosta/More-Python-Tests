


def insertInString(StringUsed, insertedItem, Position=0):
    return StringUsed[:Position] + insertedItem + StringUsed[Position:]


def placing_word_list_in_positions(RightWordList,LeftWordList,RightPositionsList,LeftPositionsList,StringUsed):

    # RightwordLength = 0

    wordLength = 0
    for i in range(len(RightPositionsList)):
        # print(i)
        # print(RightPositionsList[i])

        Rightword = RightWordList[i]+ ' '

        RightWordPosition = RightPositionsList[i] + wordLength

        print('RightWordPosition: ',RightWordPosition)

        StringUsed = insertInString(StringUsed=StringUsed,insertedItem= Rightword, Position=RightWordPosition)
        print(len(StringUsed))

        wordLength = wordLength + len(Rightword)


    for i in range(len(LeftPositionsList)):

        Leftword = ' '+ LeftWordList[i]

        print('len(Leftword) :', len(Leftword))

        print('wordLength at left: ',wordLength)
        
        LeftWordPosition = LeftPositionsList[i] + wordLength

        print('LeftWordPosition: ',LeftWordPosition)
        
        StringUsed = insertInString(StringUsed=StringUsed,insertedItem= Leftword , Position=LeftWordPosition)
        print(len(StringUsed))

        wordLength = wordLength + len(Leftword)
    # print(StringUsed)

    return StringUsed




RightWordList = ['mouse','hamister']

LeftWordList = ['lagosta']

RightPositionsList =  [0, 9]

LeftPositionsList =  [14]


StringUsed='cat meau kitty'


outputstring = placing_word_list_in_positions(RightWordList,LeftWordList,RightPositionsList,LeftPositionsList,StringUsed)


print('outputstring: ', outputstring)




