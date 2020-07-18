



# StingList="['Save Name', 'a1', 'a2', 'a3', 'a4']"

# # StingList='["Save Name", "a1", "a2", "a3", "a4"]'

# splitObj=", "

def StringListToList(StingList,splitObj):
    StingList=StingList[1:-1]

    StingList=StingList.replace("'","")
    StingList=StingList.replace('"',"")

    StingList=StingList.split(splitObj)

    return StingList



# StingListFinal = StringListToList(StingList,splitObj)


# print(StingListFinal)
