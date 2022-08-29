import json
 

 
FileToRead = 'newCustomer.json'

def GetJasonFileData(FileToRead):

    f = open(FileToRead)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)


    return  data




print(GetJasonFileData(FileToRead))

