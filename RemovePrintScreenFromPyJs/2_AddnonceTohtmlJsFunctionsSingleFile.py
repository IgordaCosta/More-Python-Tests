import pprint

import RemoveSpacesAndKeepItems



# textToChange = '''                           <button type="button" class="btn optionsbtn left btn-secondary" onclick="DeleteFromDatabase()" >Delete From Database</button>'''



# textToChange = '''<button id='something' type="button" class="btn optionsbtn left btn-secondary" "Cancel" >Cancel</button>
# '''

def AddnonceTohtmlJsFunctionsSingleLine(LineToCheck):

    textToChange = LineToCheck
    # textToChange3 = textToChange


    

    # textToChangeStayUP = textToChange.replace('"', "'").split("'")

    # textToChangeStayUP2 = textToChangeStayUP

    # functionName = ''

    # pprint.pprint(textToChange)
    # print(textToChange)

    if 'onclick' not in textToChange:

        textToChange4 = textToChange

    else:


        replaceSplitItemsList = [ ' >', '< ']

        textToChange1 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange, textToKeepList = replaceSplitItemsList)

        

        textToChange2 = textToChange1.replace("'", '"').replace(' =', '=').replace('= ', '=')

        # print(textToChange2)

        textToChangeStayUP = textToChange2.split('"')

        # print(textToChangeStayUP)

        for item in textToChangeStayUP:
            if "(" in item:
                functionName = item.replace('(','').replace(')','')

        # print(functionName)


        part2Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
                    document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName + '''() }, false); \n</script>'''
        
        # print(part2Script)

        
        # print(textToChange2)

        textToChange2List = textToChange2.split(' ')

        # print(textToChange2List)

        idItem = 'id="'

        textToChange4 = ''
        textToChange3 = ''
        if idItem in textToChange2:
            # print('yes')
            # print(textToChange2)


            for item in textToChange2List:
                # print('ok')
                textToChange3 = ''

                if idItem in item:
                    # print(item)

                    item2 = item.replace(idItem, '').replace('"','')
                    # print(item2)
                    textToChange3 = " " + idItem +  functionName  +  " " + item2 + '" '

                    textToChange4 = textToChange4 + textToChange3

                else:
                    textToChange4 = textToChange4 + item


            # print(textToChange4)

            replaceItem = 'onclick="' + functionName + '()"'

            # textToChange3List00 = textToChange3List


            # textToChange4 = ' '.join(textToChange3List)

            textToChange04 = textToChange4.replace(replaceItem, '')

            # print(textToChange04)


        else:
            
            # print(textToChange2List)     

            textToChange3List = []
            for item in range(len(textToChange2List)):

                # print(textToChange2List[item])

                if item == 0:
                    itemChecked = textToChange2List[item] + " " + idItem + functionName  +  '"'
                    # print(textToChange2List[item])
                    # print(itemChecked)
                    
                    

                else:
                    # print(textToChange2List[item])
                    # itemChecked = textToChange4 + textToChange2List[item] + '"'
                    itemChecked = textToChange4 + textToChange2List[item]

                textToChange3List.append(itemChecked)


            # print(textToChange3List)

            replaceItem = 'onclick="' + functionName + '()"'

            # textToChange3List00 = textToChange3List


            textToChange4 = ' '.join(textToChange3List)

            textToChange04 = textToChange4.replace(replaceItem, '')

        textToChange4 = textToChange04 + "\n\n" + part2Script + '\n'

        # print(textToChange4)


    # print(textToChange4)
    return textToChange4


    # else:


    #     # print(textToChange)

    #     textToChange4 = textToChange


    
    # print(textToChange4)
            #     else:
            #         itemChecked =  " " + idItem + functionName  +  " "

            #     textToChange4 = textToChange4 + itemChecked

            

                



                
                  




        





        # for item in textToChangeStayUP:
        #     if 'on' in item:


        # print(textToChangeStayUP)

        # functionName = textToChangeStayUP[item + 1].replace('(', '').replace(')', '').replace("'", '').replace('"', '').strip()


        # # print(functionName)

        # part1Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
        #             document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName + '''() }, false); \n</script>'''


        # print(part1Script)



    # else:
    #     # print('no')
    #     pass


    # if '!--' in textToChange:
    #     pass
    # else:
    # for item in range(len(textToChangeStayUP)):

    #     pprint.pprint(textToChangeStayUP[item])
        # if 'onclick' not in textToChangeStayUP[item]:

        # if '()' not in textToChangeStayUP[item]:
        #     print( textToChangeStayUP[item])
            

        # else:

        # # if 'onclick' in textToChangeStayUP[item]:
        #     functionName = textToChangeStayUP[item + 1].replace('(', '').replace(')', '').replace("'", '').replace('"', '').strip()


        #     # print(functionName)

        #     part1Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
        #                 document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName + '''() }, false); \n</script>'''
        

        #     # print(part1Script)    


        #     if '(' in textToChange3:
        #         textToChange3.replace('= ', '=').replace(' =', '=').strip()

        #         # print(textToChange3)

        #         replaceSplitItemsList = [ ' >', '< ']


        #         textToChange4 = RemoveSpacesAndKeepItems.RemoveSpacesAndKeepItems(inputText= textToChange3, textToKeepList = replaceSplitItemsList)

        #         textToChange3 = textToChange4



        #     if 'id' in textToChange3:

                
        
        #         partItemCallerList = textToChange3.replace("'",'"').replace('id="','id="' + functionName + ' ' ).split(' ')
                
        #         partItemCallerList2 = []
        #         for item in partItemCallerList:
        #             if 'onclick' in item:
        #                 pass
        #             else:
        #                 partItemCallerList2.append(item)

        #         partItemCaller = ' '.join(partItemCallerList2)


        #     else:
        #         textToChangeList = textToChange3.split(' ')


        #         textToChangeList2 = []
        #         for item in textToChangeList:
        #             if 'onclick' in item:
        #                 pass
        #             else:
        #                 textToChangeList2.append(item)

        #         partItemCaller = ''
        #         if len(textToChangeList2[0]) == 1:
        #             ititialValue = str(textToChangeList2[0] + textToChangeList2[1])
        #         else:
        #             ititialValue = str(textToChangeList2[0])
                    
        #         partItemCaller = ititialValue +   ' id=' + '"' + functionName + '" ' + ' '.join(textToChangeList2).replace(ititialValue, '')



        #     textToChange4 =   partItemCaller + '\n' +  part1Script + '\n'

        #     # print(textToChange4)

        #     # return textToChange4



    





def AddnonceTohtmlJsFunctionsSingleFile(pathUsed, fileName):

    with open(pathUsed + fileName, "r",  encoding='latin-1')  as fileUsed:
        ListOfLines = fileUsed.readlines()

        # print(ListOfLines)


    
    # print(AddnonceTohtmlJsFunctionsSingleLine)
    
          

    LineToChange2 = []  
    for LineToChange in ListOfLines:

        # print(LineToChange)

        lineChanged = AddnonceTohtmlJsFunctionsSingleLine(LineToCheck = LineToChange)

        # print(lineChanged)

        LineToChange2.append(lineChanged)


    # pprint.pprint(LineToChange2)

    

    with open(pathUsed + fileName, "w",  encoding='latin-1') as fileUsed2:
        
        fileUsed2.writelines(LineToChange2)





# print(AddnonceTohtmlJsFunctionsSingleLine(LineToCheck=textToChange))


pathUsed = r'C:\Users\Tigereye\Desktop\htmlChangeTest' + '\\'
fileName = 'index.html'

AddnonceTohtmlJsFunctionsSingleFile(pathUsed, fileName)
        









