from docx import Document


WordToCheck= 'Ÿ'

wordDocunent = r'C:\Users\IgorDC\Desktop\PydocTest\TestChanged5.docx'

document = Document(wordDocunent)

LengthOfWordToCheck = len(WordToCheck)

WordTextLocations=[]
totalLengthWords=0
for paragraph in document.paragraphs:
    for letter in paragraph.text:
    # # for wordText in paragraph.text:
    # ParagraphViewed = paragraph.text
    # # if WordToCheck in paragraph.text:
    # WordList = ParagraphViewed.split(' ')
    # for word in WordList:
    #     LengthOFword= len(word)
    #     # print(word)
        # print(letter)
        totalLengthWords = totalLengthWords + 1 
        if WordToCheck == letter:
            AmountOfTimesWordApeared = len(WordTextLocations)+1

            AmountOfLettersToGoBack= LengthOfWordToCheck * AmountOfTimesWordApeared

            WordTextLocations.append(totalLengthWords - AmountOfLettersToGoBack)


print(totalLengthWords)

print(WordTextLocations)





        # for wordText in sentence:c
            # wordText= word
#             print(wordText)

#             lengthWord=len(wordText)
#             totalLengthWords = totalLengthWords + lengthWord

#             # wordText = word.text
#             # lengthWord=len(wordText)
#             # print(word.text)
#             # totalLengthTableWords = totalLengthTableWords + lengthWord
                
#             if WordToCheck == wordText:
#                 AmountOfTimesWordApeared = len(WordTextLocations)+1

#                 AmountOfLettersToGoBack= LengthOfWordToCheck * AmountOfTimesWordApeared

#                 WordTextLocations.append(totalLengthWords - AmountOfLettersToGoBack)

# print(totalLengthWords)

# print(WordTextLocations)
        

        # print paragraph.text
        # paragraph.text = 'new text containing ocean'

# To search in Tables as well, you would need to use something like:

tableTextLocations = []
totalLengthTableWords=0
for table in document.tables:
    for row in table.rows:
        for cell in row.cells:
            cellText = cell.text
            lengthWord=len(cellText)
            # print(word.text)
            totalLengthTableWords = totalLengthTableWords + lengthWord
                
            if WordToCheck == cellText:
                AmountOfTimesWordApeared = len(tableTextLocations)+1

                AmountOfLettersToGoBack= LengthOfWordToCheck * AmountOfTimesWordApeared

                tableTextLocations.append(totalLengthTableWords - AmountOfLettersToGoBack)

print(totalLengthTableWords)

print(tableTextLocations)