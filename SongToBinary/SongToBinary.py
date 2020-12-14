import sys
import os
import base64

import time

millis = int(round(time.time() * 1000))

print(millis)

# SongName='SoundTest3.m4a'

SongName='video3Sec.mp4'

numberOfItens=25

cwdUsed=os.getcwd()

# print(cwdUsed+'\\')

Filelofcation=cwdUsed+'\\'+ SongName

BinaryOptions=['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010', '11011', '11100', '11101', '11110', '11111', '100000', '100001', '100010', '100011']


valueUsed=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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




           
