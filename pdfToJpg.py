from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path





def pdfToJpg(FolderLocation,PdfFileName,OutputFilename):


    

    if len(OutputFilename.split(".")) >1:

        remove=OutputFilename.split(".")[-1]
        OutputFilename=OutputFilename.strip("."+remove)

    


    PdfFileNameFinal=FolderLocation+PdfFileName


    print('PdfFileNameFinal',PdfFileNameFinal)
    
    images = convert_from_path(PdfFileNameFinal)

    
    i=0
    for page in images:
        i=i+1
        pagefilename=FolderLocation +OutputFilename+"_"+str(i)+'.jpg'
        page.save(pagefilename, 'JPEG')
        

    print("Done")

    




# FolderLocation="C:\\Users\\IgorDC\\Downloads\\"

# PdfFileName="WeddingContract.pdf"

# OutputFilename='PdfFileNameFinal'




# pdfToJpg(FolderLocation=FolderLocation,PdfFileName=PdfFileName,OutputFilename=OutputFilename)