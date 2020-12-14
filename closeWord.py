import win32com.client as win32



# newFileLocation="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"

# doc = docx.Document(newFileLocation) 
# print(doc)


fileName="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"


word = win32.gencache.EnsureDispatch('Word.Application')



# if the user is with its active window on this file it will work however
# if the active window is on a diferent file sometimes it will say 
# that the document is closed for editing which breaks the code

# #fix this

try:
    word.DisplayAlerts = False
    wd = word.Documents.Open(fileName)
    word.DisplayAlerts = False
    wd.Close(True)

    word.Quit()
    print("done")
except Exception as e:
    print(e)
    print('exception ran')
    map(lambda book: book.Close(False), word.Documents)
    word.Quit()


# # excel.Visible = False


# word.ScreenUpdating = False
# word.DisplayAlerts = False

# # help(word)


# wd.Close(True)

# # word.Quit()

# # word.Application.Quit()



# map(lambda book: book.Close(False), word.Documents)
# word.Quit()
