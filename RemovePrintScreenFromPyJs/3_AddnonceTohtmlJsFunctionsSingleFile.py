# import pprint
import os

import RemoveSpacesAndKeepItems







def AddnonceTohtmlJsFunctionsSingleLine(LineToCheck):

    textToChange = LineToCheck

    nonceUsed = "sdfgsmb3456jmbnmhgh767667dfga==tY2sg"

    nonceUsed1 =  nonceUsed + "'"


    





    if 'onclick' not in textToChange:

        if '()' not in textToChange:

            textToChange4 = textToChange

        else:

            replaceSplitItemsList = [ ' >', '< ']

            textToChange1 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange, textToKeepList = replaceSplitItemsList)

            textToChange1Temp = textToChange1.split('>')

            # print(textToChange1Temp)



            

            # print(textToChange1.replace(textToChange1Temp[0], textToChange1Temp[0] + " nonce='"+ nonceUsed1))

            textToChange4 = textToChange1.replace(textToChange1Temp[0], textToChange1Temp[0] + " nonce='"+ nonceUsed1)

            # print(textToChange4)

    else:


        replaceSplitItemsList = [ ' >', '< ']

        textToChange1 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange, textToKeepList = replaceSplitItemsList)

        

        textToChange2 = textToChange1.replace("'", '"').replace(' =', '=').replace('= ', '=')

        # print(textToChange2)


        textToChangeStayUP = textToChange2.split('"')


        for item in textToChangeStayUP:
            # print(item)
            if 'this.parentElement.classList.add(' in item:
                functionName='Hiddenitem'
                functionName2 = 'onclick="this.parentElement.classList.add("hidden")'

            elif "(" in item:
                functionName = item.replace('(','').replace(')','')
                functionName2 = functionName + '()'

            else:
                pass



        part2Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
                    document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName2 + ''' }, false); \n</script>'''
        

        
        print(part2Script)

        textToChange2List = textToChange2.split(' ')


        idItem = 'id="'

        textToChange4 = ''
        textToChange3 = ''
        if idItem in textToChange2:


            for item in textToChange2List:
                textToChange3 = ''

                # print(item)

                if idItem in item:

                    item2 = item.replace(idItem, '').replace('"','')

                    # print(item)
                    
                    textToChange3 = " " + idItem +  functionName  +  " " + item2 + '" '

                    textToChange4 = textToChange4 + textToChange3

                else:
                    textToChange4 = textToChange4 + item.strip() + ' '

                # print(textToChange4)



            replaceItem = 'onclick="' + functionName + '()"'




            textToChange04 = textToChange4.replace(replaceItem, '').replace('" >', '">')

            # print(textToChange04)



        else:
            

            textToChange3List = []
            for item in range(len(textToChange2List)):


                if item == 0:
                    itemChecked = textToChange2List[item] + " " + idItem + functionName  +  '"'
                    
                    

                else:
                    itemChecked = textToChange4 + textToChange2List[item]

                textToChange3List.append(itemChecked)



            replaceItem = 'onclick="' + functionName + '()"'




            textToChange4 = ' '.join(textToChange3List)

            textToChange04 = textToChange4.replace(replaceItem, '')

        textToChange4 = textToChange04 + "\n\n" + part2Script + '\n'



    return textToChange4




def AddnonceTohtmlJsFunctionsSingleFile(pathUsed, fileName):

    with open(pathUsed + fileName, "r",  encoding='latin-1')  as fileUsed:
        ListOfLines = fileUsed.readlines()


    LineToChange2 = []  
    for LineToChange in ListOfLines:



        lineChanged = AddnonceTohtmlJsFunctionsSingleLine(LineToCheck = LineToChange)

        # print(lineChanged)


        # LineToChange2.append(lineChanged)



    

    # with open(pathUsed + fileName, "w",  encoding='latin-1') as fileUsed2:
        
    #     fileUsed2.writelines(LineToChange2)







pathUsed = r'C:\Users\Tigereye\Desktop\htmlChangeTest' + '\\'
fileName = 'dragAndDrop.html'

AddnonceTohtmlJsFunctionsSingleFile(pathUsed, fileName)
        



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
        # AddBlockToPrintsInPythonJavascriptFiles(pathUsed = LocationToCheck , fileName = Filetocheck)
        AddnonceTohtmlJsFunctionsSingleFile(pathUsed = LocationToCheck, fileName= Filetocheck)









