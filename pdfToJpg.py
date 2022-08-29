from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

from pdf2image import convert_from_path





def pdfToJpg(PdfFileName,OutputFilename, FolderLocation='', diferetiate=True):


    

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
        if len(images) >1:
            newFileName=OutputFilename+"_"+str(i)+'.jpg'
        else:
            newFileName=OutputFilename+'.jpg'

        pagefilename=FolderLocation +newFileName

        page.save(pagefilename, 'JPEG')
        
        if diferetiate:
            filenames.append(newFileName)

        else:
            filenames.append(pagefilename)
        

    print("Done")

    if diferetiate:
        if i==1:
            return newFileName
        else:
            return filenames

    else:
        return filenames

    




# # FolderLocation="C:\\Users\\IgorDC\\Desktop\\"

# FolderLocation =r'C:\Users\Tigereye\Desktop' + '\\'

# # PdfFileName="WeddingContract.pdf"

# # OutputFilename='WeddingContract'



# PdfFileName="dadosMulta.facesIsabela.pdf"
# OutputFilename='dadosMultaFacesIsabela'



# pdfToJpg(FolderLocation=FolderLocation,PdfFileName=PdfFileName,OutputFilename=OutputFilename)