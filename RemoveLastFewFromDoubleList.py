


listToRemoveItens = [['nomecarro1.jpg', 'carro1', 'carro2', 'carro3', 'carro4', 'carro5', 'carro6', 'carro7', 'carro8', 'carro9', 'carro10'], ['nomeitem1.jpg', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10'], ['nomebear1.jpg', 'bear1', 'bear2', 'bear3', 'bear4', 'bear5', 'bear6', 'bear7', 'bear8', 'bear9', 'bear10'], ['nomebike1.jpg', 'bike1', 'bike2', 'bike3', 'bike4', 'bike5', 'bike6', 'bike7', 'bike8', 'bike9', 'bike10'], ['nomebee1.jpg', 'bee1', 'bee2', 'bee3', 'bee4', 'bee5', 'bee6', 'bee7', 'bee8', 'bee9', 'bee10'], ['nomebabe1.jpg', 'babe1', 'babe2', 'babe3', 'babe4', 'babe5', 'babe6', 'babe7', 'babe8', 'babe9', 'babe10'], ['nomeyat1.jpg', 'yat1', 'yat2', 'yat3', 'yat4', 'yat5', 'yat6', 'yat7', 'yat8', 'yat9', 'yat10']]

columnlist0 = "['Save Name', 'top', 'right', 'left']"

columnlist = columnlist0.replace("'",'').replace('[','').replace(']','').replace('"','').split(', ')

print(columnlist)

print(listToRemoveItens)

sizeColumn = len(columnlist)

print(sizeColumn)

listToRemoveItens2 = []
for item in listToRemoveItens:
    item2 = item[:sizeColumn]
    listToRemoveItens2.append(item2)


print(listToRemoveItens2)


