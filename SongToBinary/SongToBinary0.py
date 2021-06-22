import sys
import os
import base64
import time

import pprint

import DecimalToBinaryList







millis = int(round(time.time() * 1000))

print(millis)

# SongName='SoundTest3.m4a'

SongName='video3Sec.mp4'


# this is the number of itens in a list
numberOfItens=55

# 
# numberOfItens=40     

cwdUsed=os.getcwd()

# print(cwdUsed+'\\')

Filelofcation=cwdUsed+'\\'+ SongName

# BinaryOptions=['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111', '100000', '100001', '100010', '100011']


#  vax value e binary options for program is 256

valueUsedFor36Itens=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#this is the number of diferent "symbels per spot on the list"
dividerValue = 36

useDividerValue = True

UsevalueUsedFor36Itens = True

#this is the max number of values used in the binary list gotten from the video/sound
MaxListValue=256

# MaxListValue=80

# BinaryOptions, _ = DecimalToBinaryList.DecimalToBinaryList(MaxListValue=MaxListValue)

BinaryOptions, valueUsed = DecimalToBinaryList.DecimalToBinaryList(MaxListValue=MaxListValue)



if useDividerValue:

    MaxListValueSize = int(MaxListValue/dividerValue)*dividerValue

    BinaryOptions = BinaryOptions[:MaxListValueSize]


    if UsevalueUsedFor36Itens:

        if dividerValue == 36:

            valueUsed = valueUsedFor36Itens

            valueUsed = valueUsed*int(MaxListValue/dividerValue)
        
        else:

            valueUsed = valueUsed[:int(dividerValue)]*int(MaxListValue/dividerValue)

    else:

        valueUsed = valueUsed[:int(dividerValue)]*int(MaxListValue/dividerValue)







    


# pprint.pprint('MaxListValueSize: ' +str(MaxListValueSize))

# pprint.pprint('BinaryOptions: '+str(BinaryOptions))

# pprint.pprint('len(BinaryOptions): '+str(len(BinaryOptions)))


# pprint.pprint('valueUsed: '+str(valueUsed))

# pprint.pprint('len(valueUsed): '+str(len(valueUsed)))

# pprit("BinaryOptions: ", BinaryOptions)

# print(len(BinaryOptions))

# print(len(valueUsed))

with open(Filelofcation, 'rb') as f:
    first='tv'

    step = 0

    listUsed=[]

    file1 = open("CodesWritten.txt","w") 

    numberOfLists=0
    for c in f.read():
        if bin(c)[2:] == first:
            pass
        else: 
            value=bin(c)[2:]

            # print(value)

            if value in BinaryOptions:
                indexUsed = BinaryOptions.index(value)

                # print('indexUsed :', indexUsed)

                ValueToCheck = valueUsed[indexUsed]

                if ValueToCheck == first :
                    pass
                else:
                    # print(ValueToCheck)

                    listUsed.append(ValueToCheck)

                    first = ValueToCheck

                    step=step + 1

                    

                    if step == numberOfItens:

                        numberOfLists = numberOfLists + 1

                        step = 0

                        # print(listUsed)

                        # print(numberOfLists)

                        file1.write(str(numberOfLists) + ":          "+ str(listUsed)+"\n" )

                        # file1 = open("myfile.txt","w") 
                        # L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
                        
                        # # \n is placed to indicate EOL (End of Line) 
                        # file1.write("Hello \n") 
                        # file1.writelines(L) 
                        # file1.close() #to change file access modes 


    
                        listUsed = []


    file1.close()


millis2 = int(round(time.time() * 1000))

print(millis2)

print('it took ' ,millis2-millis, 'milliseconds to complete')




           
