import numpy

AddToTablevaluesList000 = ['first', '  the second', ' this is third', 'this is the      fourth', 'this is the     fifth', 'this is the    sixth', 'this is the  seventh', 'this is the eigth    ', 'this is the nineth   ', 'this is the tenght  ', 'this is the eleventh ' ]



AddToTablevaluesList0001 = ' '.join(str(AddToTablevaluesList000).split())
NewList = AddToTablevaluesList0001.replace('[','').replace(']','').replace('"','').replace("'",'').split(', ')
AddToTablevaluesList00 = numpy.array(NewList)




print(AddToTablevaluesList00)


print(AddToTablevaluesList00[0])


print(AddToTablevaluesList00[-1])