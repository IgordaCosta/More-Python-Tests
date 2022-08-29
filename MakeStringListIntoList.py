  #['['1314']', '98']",

finalLocationsX = "['1314'],['456']"

ListA = str(finalLocationsX).replace('[','').replace(']','').replace("'",'').split(',')


print(ListA)

print(type(ListA))



print(ListA[0])