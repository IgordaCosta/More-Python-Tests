import ReadTextFileIntoList


textFileLocation = r'C:\Users\Tigereye\Downloads\bad-girls-2021-english-yify-386674' + '\\'

textFileName = 'TexIntoListTest.srt'



def GetTextItemsFromList(textFileLocation,textFileName):


    ListGotten = ReadTextFileIntoList.ReadTextFileIntoList(textFileLocation= textFileLocation,textFileName=textFileName)


    # print(ListGotten)

    TextOnlyList = [[]]

    textSize = 0

    InListLocation = 0
    for item0 in ListGotten:

        IsIntText = False

        quoteReplace1 = ' @@%& '

        item = item0.replace("'", quoteReplace1 )

        IntItem = ''
        try:
            IntItem = int(item[0])
            IsIntText = True
        except:
            pass

        if IsIntText:
            pass
        else:
            LineSize = len(item)

            NewTextSize0 = LineSize + textSize

            if NewTextSize0< 2000:

                

                TextOnlyList[InListLocation].append(item)

                textSize = NewTextSize0
            else:
                TextOnlyList.append([])
                
                InListLocation = InListLocation +1
                TextOnlyList[InListLocation].append(item)

                NewTextSize0 = LineSize

                textSize = NewTextSize0


    # print(TextOnlyList[2])

    pediodReplace = ' $%$# '

    commaRepalce = ' &@%$ '

    quoteReplace2 = ''

    TextOnlyList2 = []
    for ListItem in TextOnlyList:
        ListItem2 = str(ListItem)[1:-1].replace('.',pediodReplace ).replace(',', commaRepalce).replace("'", quoteReplace2)

        TextOnlyList2.append(ListItem2)


    return TextOnlyList2




# print(len(GetTextItemsFromList(textFileLocation,textFileName)))













