import sys
import os
import base64
import time

import pprint

import DecimalToBinaryList

#TODO add more possible variables like uppercase and symbols to 'valueUsedFor36Itens'
#     for the way it is 'passwords' are weaker
#     add a different option for such and activate it by default
#     after adding this values scramble them manually then after by ramdom function
#     this can be done first by only providing all the caracters (not in list format) 
#     one after the other and in MS word and selecting, dragging, then droping
#     cetain areas of the word into a different location of the word (string of characters) 
#     then providing that word into a fuction that will randomise the order of characters
#     after that it will feed this string into a function that will turn this string of characters
#     into a list of characters
#     this list of characters will be used as the possible characters for this password
#     that will be generated
#     this will then be saved into a different .7z folder file

def GetUniqueBinaryListFromFile(numberOfItens,InputFileLocation,OutputFileTxtLocation):

    millis = int(round(time.time() * 1000))

    print(millis)

    # this is the number of itens in a list
    #numberOfItens=55

    Filelofcation=InputFileLocation

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


    

    with open(Filelofcation, 'rb') as f:
        first='tv'

        step = 0

        listUsed=[]

        #file1 = open("CodesWritten.txt","w") 

        file1 = open(OutputFileTxtLocation,"w") 

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

                        listUsed.append(ValueToCheck)

                        first = ValueToCheck

                        step=step + 1

                       
                        if step == numberOfItens:

                            numberOfLists = numberOfLists + 1

                            step = 0


                            file1.write(str(numberOfLists) + ":          "+ str(listUsed)+"\n" )

   
                            listUsed = []


        file1.close()


    millis2 = int(round(time.time() * 1000))

    print(millis2)

    print('it took ' ,millis2-millis, 'milliseconds to complete')



def getUniqueValuesFromList(fileTxtInput, fileTxtOutput = ''):
    
    if fileTxtOutput == '':
        fileTxtOutput = fileTxtInput

    millis = int(round(time.time() * 1000))

    print(millis)

    fileUsed = fileTxtInput


    file1 = open(fileUsed,"r") 


    inputLines=file1.readlines()


    AllDataList=[]
    for i in range(len(inputLines)):

        processLine = inputLines[i]

        processLine2 = processLine[:-1]

        processLine3 = processLine2.split('          ')[-1]

        AllDataList.append(processLine3)


    print("Number of AllDataList: " , len(AllDataList))

    UniqueAllDataList = list(set(AllDataList))

    print('Number of UniqueAllDataList :', len(UniqueAllDataList))

    difference = len(AllDataList) - len(UniqueAllDataList)

    print("difference between Unique and NonUnique values: " ,difference)

    print("% difference between Unique and NonUnique values: " ,(difference/len(AllDataList))*100 , "%")

    file1.close()

    file2 = open(fileTxtOutput,"w")


    for i in range(len(UniqueAllDataList)):
        file2.write(str(UniqueAllDataList[i]) + "\n" )


    file2.close()


    millis2 = int(round(time.time() * 1000))

    print(millis2)

    print('it took ' ,millis2-millis, 'milliseconds to complete')



def GetEspecificLineTxt(LineToGet, OutputFileTxtLocation):

    file2 = open(OutputFileTxtLocation,"r")

    Lines = file2.readlines()

    file2.close()



    LineGotten = Lines[LineToGet - 1]

    DataFromLine0 = LineGotten.replace("[", "")

    DataFromLine1 = DataFromLine0.replace("]", "")

    DataFromLine2 = DataFromLine1.replace("'", "")

    DataFromLine3 = DataFromLine2.replace(",", "")

    DataFromLine4 = DataFromLine3.replace(" ", "")

    DataFromLine = DataFromLine4.replace(str(LineToGet) + ":", "")

    print(DataFromLine)


    print('number of itens in line: ' + str(len(DataFromLine)))

            

