import RunExcelMacro



def RunCloseWordMacro(Location,excelFile,WordFile):

    
    MacroName="Macro1"

    Macro=\
    '''Sub Macro1()

        Macro1 Macro

        Dim wdApp As Word.Application
        Set wdApp = GetObject(, "Word.Application")
        wdApp.Documents("%s").Close
    End Sub
    '''%(WordFile)




    RunExcelMacro.RunExcelMacro(Location=Location,excelFile=excelFile,MacroName=MacroName,Macro=Macro,SaveChanges=0)

    print("Done Merging Cells")







Location="C:\\Users\\IgorDC\\Desktop\\"

excelFile="MacroTest.xlsx"

MacroName="Macro1"

WordFile="C:\\Users\\IgorDC\\Desktop\\barra De Progresso Igor 2.docx"


RunCloseWordMacro(Location,excelFile,WordFile)
