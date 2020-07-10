import ExcelToPdf
import pdfToJpg


def excelToJpg(excelFileName,FolderLocation,OutputFilename):

    remove=excelFileName.split(".")[-1]
    pdfFileName=excelFileName.strip("."+remove)

    pdfFileName=pdfFileName+".pdf"



    (unnecessaryFile)=ExcelToPdf.ExcelToPdf(excelFileName=excelFileName,pdfFileName=pdfFileName,excelFolderSavePath=FolderLocation,pdfFolderSavePath=FolderLocation)



    pdfToJpg.pdfToJpg(FolderLocation=FolderLocation,PdfFileName=pdfFileName,OutputFilename=OutputFilename)

    print("unnecessaryFile: ",unnecessaryFile)




excelFileName="emptyExcelFile.xlsx"


FolderLocation="C:\\Users\\IgorDC\\Desktop\\"

OutputFilename="emptyExcelJPGFile.jpg"


excelToJpg(excelFileName,FolderLocation,OutputFilename)