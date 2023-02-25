

# textToChange = '''<div>
#         <button type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
#     </div>'''

textToChange = '''<button id='something' type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
'''

textToChange3 = textToChange


#       <script nonce='sdfgsmb3456jmbnmhgh767667dfga==tY2sg'>
#                   document.getElementById ("UnhideScroll"). addEventListener ('click', function (e) { UnhideScroll() }, false);
#       </script>


textToChange1 = textToChange.split('onclick')[-1]

# print(textToChange1)

textToChange2 = textToChange1.split('>')[0].replace('"', '').replace("'","").replace('(','').replace(')','').replace('=', '').strip()

# print(textToChange2)


# textToChangeStayUP = textToChange.split("'")

# print(len(textToChangeStayUP))

# if len(textToChangeStayUP) == 1:
#     textToChangeStayUP = textToChange.split('"')

textToChangeStayUP = textToChange.replace('"', "'").split("'")

# print(textToChangeStayUP)

functionName = ''
textToChangeStayUP2 = []
for item in range(len(textToChangeStayUP)):
    if 'onclick' in textToChangeStayUP[item]:
        functionName = textToChangeStayUP[item + 1].replace('(', '').replace(')', '').replace("'", '').replace('"', '').strip()

    elif '(' in textToChangeStayUP[item]:
        pass
    else:
        textToChangeStayUP2.append(textToChangeStayUP[item])

# print(textToChangeStayUP2)

textToChangeStayUP3 = '"'.join(textToChangeStayUP2)

# print(textToChangeStayUP3)

# print(functionName)


part1Script = '''<script nonce="sdfgsmb3456jmbnmhgh767667dfga==tY2sg">
                   document.getElementById ("''' + functionName + '''"). addEventListener ("click", function (e) { '''+ functionName + '''() }, false); \n</script>'''


# print(part1Script)



# print(textToChange)

# textToChange2 = '''<button  type="button" class="btn optionsbtn left btn-secondary" onclick="Cancel()" >Cancel</button>
# '''

textToChange3.replace('= ', '=').replace(' =', '')

# print(textToChange3)

if '(' in textToChange3:
    if 'id' in textToChange3:
        partItemCallerList = textToChange3.replace("'",'"').replace('id="','id="' + functionName + ' ' ).split(' ')
        
        partItemCallerList2 = []
        for item in partItemCallerList:
            if 'onclick' in item:
                pass
            else:
                partItemCallerList2.append(item)

        partItemCaller = ' '.join(partItemCallerList2)

        # print(partItemCaller)

    else:
        textToChangeList = textToChange3.split(' ')

        # print(textToChangeList)

        textToChangeList2 = []
        for item in textToChangeList:
            if 'onclick' in item:
                pass
            else:
                textToChangeList2.append(item)

        partItemCaller = ''
        if len(textToChangeList2[0]) == 1:
            ititialValue = str(textToChangeList2[0] + textToChangeList2[1])
        else:
            ititialValue = str(textToChangeList2[0])
            
        partItemCaller = ititialValue +   ' id=' + '"' + functionName + '" ' + ' '.join(textToChangeList2).replace(ititialValue, '')

        # print(partItemCaller)



    print(partItemCaller + '\n' + part1Script)
    









