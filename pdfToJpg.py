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

    filenames=[]
    i=0
    for page in images:
        i=i+1
        newFileName=OutputFilename+"_"+str(i)+'.jpg'

        pagefilename=FolderLocation +newFileName

        page.save(pagefilename, 'JPEG')
        
        filenames.append(newFileName)
        

    print("Done")
    if i==1:
        return newFileName
    else:
        return filenames

    




# FolderLocation="C:\\Users\\IgorDC\\Downloads\\"

# PdfFileName="WeddingContract.pdf"

# OutputFilename='PdfFileNameFinal'




# pdfToJpg(FolderLocation=FolderLocation,PdfFileName=PdfFileName,OutputFilename=OutputFilename)