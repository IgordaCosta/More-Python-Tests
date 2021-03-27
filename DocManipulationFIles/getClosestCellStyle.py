# uses prorams that have the       from docx import Document 

def getClosestCellStyle(itemList, document):

    documentCells = document.tables[int(itemList[0])].rows[int(itemList[1])].cells

    stopCheck = False
    for cell0 in range(len(documentCells)-1):

        if stopCheck == False:
            CellToCheck = len(documentCells)-1 - cell0
            Cc = document.tables[int(itemList[0])].rows[int(itemList[1])].cells[CellToCheck].paragraphs[0]
            if Cc.runs == []:
                pass
            else:
               stopCheck = True
    if stopCheck:
        r1 = document.tables[int(itemList[0])].rows[int(itemList[1])].cells[CellToCheck].paragraphs[0]

        StyleGotten = r1.runs[0].style

    else: 
        StyleGotten = ''
    
    return StyleGotten



# Style = getClosestCellStyle(itemList, document)

# print(Style)