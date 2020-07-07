from win32com import client
import win32api
import pathlib
### pip install pypiwin32 if module not found
def ExcelToPdf(excelFileName,pdfFileName,excelFolderSavePath,pdfFolderSavePath):
    excel_file = excelFileName
    pdf_file = pdfFileName
    excel_path = (excelFolderSavePath + excel_file)
    pdf_path = (pdfFolderSavePath+ pdf_file)
    excel = client.dynamic.Dispatch("Excel.Application")
    excel.Visible = 0
    wb = excel.Workbooks.Open(excel_path)
    ws = wb.Worksheets[0]
    try:
        wb.SaveAs(pdf_path, FileFormat=57)
    except Exception as e:
        print("Failed to convert")
        print(str(e))
    finally:
        wb.Close()
        excel.Quit()
        print("DONE single Excel to Pdf")


# excelFileName='testFile.xlsx'

# pdfFileName='testFile.pdf'

# excelFolderSavePath='C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\'

# pdfFolderSavePath='C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\'


# ExcelToPdf(excelFileName=excelFileName,pdfFileName=pdfFileName,excelFolderSavePath=excelFolderSavePath,pdfFolderSavePath=pdfFolderSavePath)