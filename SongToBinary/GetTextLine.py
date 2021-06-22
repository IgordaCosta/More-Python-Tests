import time

millis = int(round(time.time() * 1000))

print(millis)


# fileUsed='CodesWritten3SecAudio10Line.txt'

# fileUsed= 'CodesWritten3SecAudio.txt'

# fileUsed = 'CodesWritten3sVideo.txt'

# fileUsed = 'CodesWritten3sVideo25Digit.txt'



# fileUsed = 'CodesWritten3sVideo25Digit256bits36choices.txt'

fileUsed = 'CodesWritten3sVideo55Digit.txt'


file1 = open(fileUsed,"r") 
# print(file1.readlines())

inputLines=file1.readlines()


AllDataList=[]
for i in range(len(inputLines)):

    processLine = inputLines[i]

    # print(processLine[:-2])

    processLine2 = processLine[:-1]

    # print(processLine2)

    processLine3 = processLine2.split('          ')[-1]

    # print(processLine3)

    AllDataList.append(processLine3)


print("Number of AllDataList: " , len(AllDataList))

UniqueAllDataList = list(set(AllDataList))

print('Number of UniqueAllDataList :', len(UniqueAllDataList))

difference = len(AllDataList) - len(UniqueAllDataList)

print("difference between Unique and NonUnique values: " ,difference)

print("% difference between Unique and NonUnique values: " ,(difference/len(AllDataList))*100 , "%")

file1.close()

file2 = open("CodesUniqueWritten.txt","w")


for i in range(len(UniqueAllDataList)):
    file2.write(str(UniqueAllDataList[i]) + "\n" )


file2.close()




    



    




file1.close() 



millis2 = int(round(time.time() * 1000))

print(millis2)

print('it took ' ,millis2-millis, 'milliseconds to complete')