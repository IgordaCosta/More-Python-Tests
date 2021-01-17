from PyPDF2 import PdfFileReader, PdfFileWriter
# import datetime

import time
 














def GetPdfFromAnotherPdf(OrigianlPdfDocument,Location,FromPage,ToPage):
    # currentDT = datetime.datetime.now()

    PdfName=Location+"\\"+OrigianlPdfDocument

    print(PdfName)

    pdf = PdfFileReader(PdfName)

    Extension = OrigianlPdfDocument.split(".")[-1]

    ExtensionSize =len(Extension)+1

    # outputFilename= OrigianlPdfDocument[:-ExtensionSize]+str(currentDT)
    # outputFilename= OrigianlPdfDocument[:-ExtensionSize]+str(time.time())+"."+Extension


    maxPageSize = pdf.getNumPages()

    print('maxPageSize: ',maxPageSize)

    if ToPage > maxPageSize:
        ToPage = maxPageSize


    if FromPage < ToPage:

        pdf_writer = PdfFileWriter()
        current_page = pdf.getPage(FromPage)
        pdf_writer.addPage(page=current_page)

        for page in range(FromPage+1,ToPage):
            
            current_page = pdf.getPage(page)
            # pdf_writer.addPage(page=current_page)
            

            pdf_writer.mergePage(page=current_page)

        outputFilename= OrigianlPdfDocument[:-ExtensionSize]+str(time.time())+"_"+str(page)+"."+Extension

        with open(Location+"\\"+outputFilename, "wb") as out:
            pdf_writer.write(out)

            print("created", outputFilename)

    else:
        print('FromPage greate than ToPage')





FromPage = 1

ToPage = 4

OrigianlPdfDocument='WeddingContract.pdf'

Location=r'C:\Users\IgorDC\Desktop\StripPdfPages'

GetPdfFromAnotherPdf(OrigianlPdfDocument,Location,FromPage,ToPage)