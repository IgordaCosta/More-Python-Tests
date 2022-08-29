import re


AddToTablevaluesList0 = 'te&$*&xt 2zz,zz text'


spaceReplaceData = '$%3&*&'

# AddToTablevaluesList00 = re.sub("[^A-Za-z0-9]","",AddToTablevaluesList0)

AddToTablevaluesList00 = re.sub("[^A-Za-z0-9,\s]","",AddToTablevaluesList0)

AddToTablevaluesList = AddToTablevaluesList00.replace(' ', '$%3&*&')


print(AddToTablevaluesList)