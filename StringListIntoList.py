# # StringList="['Save Name', 'a1', 'a2', 'a3', 'a4']"

# StringList='["Save Name", "a1", "a2", "a3", "a4"]'


def StringListIntoList(StringList,brakets=True,Splitter=", "):
    if brakets:
        StringList=StringList[1:-1]

    StringList=StringList.replace("'","")
    StringList=StringList.replace('"',"")

    StringList=StringList.split(Splitter)
   

    return StringList



# print(StringListIntoList(StringList))



