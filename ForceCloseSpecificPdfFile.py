import os

def ForceCloseSpecificPdfFile(fileName, Program="Adobe Acrobat Reader DC"):

    try:
        os.system('cmd /c "taskkill /F /FI "WindowTitle eq '+fileName+' - '+Program+'" /T"')

    except Exception:
        print("Excel file "+fileName+" was not found")




fileName="test2.pdf"

ForceCloseSpecificPdfFile(fileName=fileName)