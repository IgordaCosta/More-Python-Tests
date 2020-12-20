import win32com.client as win32



# newFileLocation="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

# doc = docx.Document(newFileLocation) 
# print(doc)


fileName="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"



def closeWord(fileName):
    word = win32.gencache.EnsureDispatch('Word.Application')

    returnValue=word.Documents.Open(fileName).Close(True)

    # print(returnValue)



# closeWord(fileName)


