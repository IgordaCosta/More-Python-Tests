import os, PyPDF2










def JoinPdfs(Folderlocation,nameOfNewFile,desiredFileType):

    pdf2merge =[]
    for filename in os.listdir(Folderlocation):
        if filename.endswith(".pdf"):
            if (filename.split("_")[0]==desiredFileType):
                pdf2merge.append(filename)

    print(pdf2merge)

    pdf2merge.sort()

    print(pdf2merge)

    pdfWriter = PyPDF2.PdfFileWriter()

    for filename in pdf2merge:

        pdfFileObj = open(Folderlocation+filename,"rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
        for pageNumber in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNumber)
            pdfWriter.addPage(pageObj)
            
        
        print(filename+"was appended")

                
    pdfOutput = open(Folderlocation+nameOfNewFile+'.pdf','wb')

    pdfWriter.write(pdfOutput)

    pdfOutput.close()

    print("Done Join Pdfs")






# Folderlocation="C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\"

# nameOfNewFile="NewFileJoined"
# desiredFileType="testFile"



# JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType)



