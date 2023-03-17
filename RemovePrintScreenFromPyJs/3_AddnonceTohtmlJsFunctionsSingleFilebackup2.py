import os

import RemoveSpacesAndKeepItems







def AddnonceTohtmlJsFunctionsSingleLine(LineToCheck):

    textToChange = LineToCheck

    nonceUsed = "sdfgsmb3456jmbnmhgh767667dfga==tY2sg"

    nonceUsed1 =  nonceUsed + "'"


    





    if 'onclick' not in textToChange:

        if '()' not in textToChange:

            textToChangeSetaTest = textToChange.replace(' ','')

            print(textToChangeSetaTest)
            if textToChangeSetaTest == '<script>':

                # print(textToChange)

                textToChangeReplacement = '<script '+ nonceUsed1 + '>'

                textToChange4 = textToChange.replace(textToChange, textToChangeReplacement)

            else:

                textToChange4 = textToChange

    #     else:

    #         replaceSplitItemsList = [ ' >', '< ']

    #         textToChange1 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange, textToKeepList = replaceSplitItemsList)

    #         textToChange1Temp = textToChange1.split('>')



            


    #         textToChange4 = textToChange1.replace(textToChange1Temp[0], textToChange1Temp[0] + " nonce='"+ nonceUsed1)


    # else:


    #     replaceSplitItemsList = [ ' >', '< ']

    #     textToChange1 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange, textToKeepList = replaceSplitItemsList)


    #     textToChange2 = textToChange1.replace("'", '"').replace(' =', '=').replace('= ', '=')


    #     textToChangeStayUP = textToChange2.split('"')


        
    #     for item in textToChangeStayUP:
    #         if "(" in item:
    #             functionName = item.replace('(','').replace(')','')
    #         else:
    #             functionName = 'XXXX'



    #     part2Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
    #                 document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName + '''() }, false); \n</script>'''
        

        

    #     textToChange2List = textToChange2.split(' ')


    #     idItem = 'id="'

    #     textToChange4 = ''
    #     textToChange3 = ''
    #     if idItem in textToChange2:


    #         for item in textToChange2List:
    #             textToChange3 = ''

    #             if idItem in item:

    #                 item2 = item.replace(idItem, '').replace('"','')
    #                 textToChange3 = " " + idItem +  functionName  +  " " + item2 + '" '

    #                 textToChange4 = textToChange4 + textToChange3

    #             else:
    #                 textToChange4 = textToChange4 + item



    #         replaceItem = 'onclick="' + functionName + '()"'




    #         textToChange04 = textToChange4.replace(replaceItem, '')



    #     else:
            

    #         textToChange3List = []
    #         for item in range(len(textToChange2List)):


    #             if item == 0:
    #                 itemChecked = textToChange2List[item] + " " + idItem + functionName  +  '"'
                    
                    

    #             else:
    #                 itemChecked = textToChange4 + textToChange2List[item]

    #             textToChange3List.append(itemChecked)



    #         replaceItem = 'onclick="' + functionName + '()"'




    #         textToChange4 = ' '.join(textToChange3List)

    #         textToChange04 = textToChange4.replace(replaceItem, '')

    #     textToChange4 = textToChange04 + "\n\n" + part2Script + '\n'



    # return textToChange4




def AddnonceTohtmlJsFunctionsSingleFile(pathUsed, fileName):

    with open(pathUsed + fileName, "r",  encoding='latin-1')  as fileUsed:
        ListOfLines = fileUsed.readlines()


    LineToChange2 = []  
    for LineToChange in ListOfLines:



        lineChanged = AddnonceTohtmlJsFunctionsSingleLine(LineToCheck = LineToChange)



    #     LineToChange2.append(lineChanged)



    

    # with open(pathUsed + fileName, "w",  encoding='latin-1') as fileUsed2:
        
    #     fileUsed2.writelines(LineToChange2)








        



# def AddNonceToLineInLocation(LocationToCheck):
#     LocationFileList = os.listdir(LocationToCheck)


#     fileToCheck2 = []
#     for fileToCheck in LocationFileList:
#         if '.' in fileToCheck:
#             if ".vscode" in fileToCheck:
#                 pass
#             else:
#                 fileToCheck2.append(fileToCheck)


#     for Filetocheck in fileToCheck2:
#         AddnonceTohtmlJsFunctionsSingleFile(pathUsed = LocationToCheck, fileName= Filetocheck)




LocationToCheck = r'C:\Users\Tigereye\Desktop\htmlChangeTest' + '\\'


# AddNonceToLineInLocation(LocationToCheck)

fileName = 'dragAndDrop.html'

AddnonceTohtmlJsFunctionsSingleFile(pathUsed=LocationToCheck, fileName=fileName)









