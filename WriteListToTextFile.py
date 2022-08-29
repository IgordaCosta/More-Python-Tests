
# a_list = ['Be careful.\n', '\n', '1441\n', '01:28:11,500 --> 01:28:12,296\n', 'Good luck!']       



# textFileLocation = r'C:\Users\Tigereye\Downloads\bad-girls-2021-english-yify-386674' + '\\'

# textFileName = 'TextFIleWriteTest.srt'


# ListToWrite = ['açççç', 'bÔ', 'cÈ']

def WriteListToTextFile(textFileLocation,textFileName, ListToWrite ):
    a_list = ListToWrite

    textfile = open(textFileLocation + textFileName, "w", encoding='utf-8')


    for element in a_list:

        textfile.write(element+' \n')

    textfile.close()




# WriteListToTextFile(textFileLocation,textFileName, ListToWrite )