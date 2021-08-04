import win32com.client as win32



# newFileLocation="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

# doc = docx.Document(newFileLocation) 
# print(doc)


# fileName="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

#### Add this close function method to the excel and if possible the pdf and image documents 

def closeWord(fileName):
    word = win32.gencache.EnsureDispatch('Word.Application')

    try:
        returnValue=word.Documents.Open(fileName).Close(True)
        print("AllOK")
    except:
        print('SheetIsOpenAndHasChanges')

    # print(returnValue)


def closeOpenWord(fileName):
    word = win32.gencache.EnsureDispatch('Word.Application')

    word.Visible = True
            
    word.ScreenUpdating = True
    word.DisplayAlerts = True
    word.EnableEvents = True
    word.WindowState = win32.constants.xlMaximized  # this works for me 

    try:
        
        returnValue=word.Documents.Open(fileName)
        print("AllOK")
    except:
        print('SheetIsOpenAndHasChanges')


