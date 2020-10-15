import ExcelToPdf
import pdfToJpg
import os

# this file convests excel file to jpg file


def excelToJpg(excelFileName,FolderLocation,OutputFilename):

    remove=excelFileName.split(".")[-1]
    pdfFileName=excelFileName.strip("."+remove)

    pdfFileName=pdfFileName+".pdf"
    try:
        os.remove(FolderLocation+pdfFileName)
    except:
        print("this file was already deleted or does not exist")

    (unnecessaryFile,noError)=ExcelToPdf.ExcelToPdf(excelFileName=excelFileName,pdfFileName=pdfFileName,excelFolderSavePath=FolderLocation,pdfFolderSavePath=FolderLocation)


    if noError:
        OutputFinalFilename=pdfToJpg.pdfToJpg(FolderLocation=FolderLocation,PdfFileName=pdfFileName,OutputFilename=OutputFilename)

        print("unnecessaryFile: ",unnecessaryFile)
        print("FolderLocation+pdfFileName",FolderLocation+pdfFileName)

        os.remove(unnecessaryFile)

    return OutputFinalFilename, noError




# excelFileName="emptyExcelFile.xlsx"


# FolderLocation="C:\\Users\\IgorDC\\Desktop\\"

# OutputFilename="emptyExcelJPGFile.jpg"


# excelToJpg(excelFileName,FolderLocation,OutputFilename)