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
    # utf-8
    with open(pathUsed + fileName, "r",  encoding='latin-1')  as fileUsed:
        ListOfLines = fileUsed.readlines()
        # print(ListOfLines)

        # ListOfLines = [str(item) for item in fileUsed]
        # print(ListOfLines)




    # print(ListOfLines)

    

   

    LineToChange2 = []
    for LineToChange in ListOfLines:
        # print(LineToChange)

        

        

        if '#' in LineToChange:
            # outputLine = LineToChange
            LineToChange2.append(LineToChange)
            # pass

        #### keep this code BELLOW for when needed (DO NOT DELETE!)
                                # elif LineToChange.strip() == "<head>":
                                #     replaceScriptTag1 = '<head>\n\n\t<meta http-equiv="content-security-policy" content="script-src \'nonce-sdfgsmb3456jmbnmhgh767667dfga==tY2sg\' ;object-src \'self\' app:;">'
                                #     replaceScriptTag2 = '<head>\n\n\t<meta http-equiv="content-security-policy" content="object-src \'self\' app:;">' 
                                #     LineToChange0 = LineToChange.replace(replaceScriptTag1, replaceScriptTag2)

                                #     LineToChange2.append(LineToChange0)

                                # elif "<script" in LineToChange:
                                    
                                #      replaceScriptTag = "<script nonce='sdfgsmb3456jmbnmhgh767667dfga==tY2sg'"

                                #      if replaceScriptTag in LineToChange:
                                #          pass
                                #      else:
                                #         LineToChange0 = LineToChange.replace("<script", replaceScriptTag)
                                    
                                #         LineToChange2.append(LineToChange0)
        #### keep this code ABOVE for when needed (DO NOT DELETE!)

        
        elif 'import pprint' in  LineToChange:
            # outputLine = LineToChange.replace('print(', '# print(')
            # LineToChange0 = LineToChange.replace('print(', '# print(')

            LineToChange0 = LineToChange.replace('import pprint', '# import pprint')
            
            LineToChange2.append(LineToChange0)
        
        elif 'pprint.' in  LineToChange:
            # outputLine = LineToChange.replace('print(', '# print(')
            # LineToChange0 = LineToChange.replace('print(', '# print(')

            LineToChange0 = LineToChange.replace('pprint.pprint(', '# pprint.pprint(')
            
            LineToChange2.append(LineToChange0)

        elif 'print' in  LineToChange:
            # outputLine = LineToChange.replace('print(', '# print(')
            try:
                print(LineToChange0)
                
            except:
                if 'pprint' in  LineToChange:
                    pass
                else:
                    LineToChange0 = LineToChange.replace('print(', '# print(')

                    # LineToChange0 = LineToChange.replace('pprint.p#', '# pprint')
                    
                    LineToChange2.append(LineToChange0)

        elif '//' in LineToChange:
            # outputLine = '// in line DO NOTHING'
            # pass
            LineToChange2.append(LineToChange)

        

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

    with open(pathUsed + fileName, "w",  encoding='latin-1') as fileUsed2:
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
            if ".vscode" in fileToCheck:
                pass
            else:
                fileToCheck2.append(fileToCheck)

    # print(type(fileToCheck2))

    for Filetocheck in fileToCheck2:
        AddBlockToPrintsInPythonJavascriptFiles(pathUsed = LocationToCheck , fileName = Filetocheck)




# LocationToCheck = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller4\CSSAutoFormFiller\_engine' +'\\'

LocationToCheck = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller3_2\CSSAutoFormFiller\js' +'\\'


ChangeLineInLocation(LocationToCheck)


# print("<head>".replace("<head>", '<head>\n<meta http-equiv="content-security-policy" content="script-src "nonce-sdfgsmb3456jmbnmhgh767667dfga==tY2sg" ;object-src "self" app:;"'))



