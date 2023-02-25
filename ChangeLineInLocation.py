import os
import pprint




# LineToChange = 'print("# # this is a printed line")'

# LineToChange = 'console.log("Another printed line)'

# LineToChange = 'Another line'

# ListOfLines = [
#     "#print('this is a printed line)'",
#     '// console.log("Another printed line)',
#     'Another line'



# ]



def AddBlockToPrintsInPythonJavascriptFiles(pathUsed, fileName):

    with open(pathUsed + fileName, "r",  encoding='utf-8')  as fileUsed:
        ListOfLines = fileUsed.readlines()

    # print(ListOfLines)

    

   

    LineToChange2 = []
    for LineToChange in ListOfLines:
        # print(LineToChange)
    

        if '#' in LineToChange:
            # outputLine = LineToChange
            LineToChange2.append(LineToChange)
            # pass

        elif '//' in LineToChange:
            # outputLine = '// in line DO NOTHING'
            # pass
            LineToChange2.append(LineToChange)

        elif 'print(' in LineToChange:
            # outputLine = LineToChange.replace('print(', '# print(')
            LineToChange0 = LineToChange.replace('print(', '# print(')
            LineToChange2.append(LineToChange0)

        elif 'console.log(' in LineToChange:
            # outputLine = LineToChange.replace("console.log(", "// console.log(")
            LineToChange0 = LineToChange.replace("console.log(", "// console.log(")
            LineToChange2.append(LineToChange0)

        else:
            #  outputLine = 'DO NOTHING'
            # outputLine = LineToChange
            # pass
            LineToChange2.append(LineToChange)



    # pprint.pprint(LineToChange2)

        # fileUsed.writelines(LineToChange)

    with open(pathUsed + fileName, "w",  encoding='utf-8') as fileUsed2:
        # ListOfLines = fileUsed.readlines()
        ##print(str(ListOfLines).replace("'",'').replace(',','').replace('[','').replace(']',''))

        fileUsed2.writelines(LineToChange2)
    
        # for itemtoAdd in LineToChange:
        #     fileUsed2.write(itemtoAdd)





# pathUsed = r'C:\Users\Tigereye\Desktop\RemovePrintsTest' +'\\'



# # fileName = 'FileExistInDatabaseFunction.py'

# # # fileName =  'CheckIfNameExists.js'

# # AddBlockToPrintsInPythonJavascriptFiles(pathUsed, fileName)



# LocationToCheck = r'C:\Users\Tigereye\Desktop\RemovePrintsTest' +'\\'



def ChangeLineInLocation(LocationToCheck):
    LocationFileList = os.listdir(LocationToCheck)

    # print(LocationList)

    fileToCheck2 = []
    for fileToCheck in LocationFileList:
        if '.' in fileToCheck:
            fileToCheck2.append(fileToCheck)

    # print(fileToCheck2)

    for Filetocheck in fileToCheck2:
        AddBlockToPrintsInPythonJavascriptFiles(pathUsed = LocationToCheck , fileName = Filetocheck)




# LocationToCheck = r'C:\Users\Tigereye\Desktop\RemovePrintsTest' +'\\'

# ChangeLineInLocation(LocationToCheck)