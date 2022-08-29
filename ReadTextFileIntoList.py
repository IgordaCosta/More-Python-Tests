

# textFileLocation = r'C:\Users\Tigereye\Downloads\bad-girls-2021-english-yify-386674' + '\\'

# textFileName = 'MovieSubtilteTest.srt'


def ReadTextFileIntoList(textFileLocation,textFileName):

    my_file = open(textFileLocation + textFileName, "r",  encoding='utf-8')

    content_list = my_file.readlines()

    content_list2 = []
    for item in content_list:
        item2 = item.replace('\n', '')
        content_list2.append(item2)


    return content_list2