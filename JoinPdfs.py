import os, PyPDF2










def JoinPdfs(Folderlocation,nameOfNewFile,desiredFileType,splitSymbol="_"):

    pdf2merge =[]
    for filename in os.listdir(Folderlocation):
        if filename.endswith(".pdf"):
            if (filename.split(splitSymbol)[0]==desiredFileType):
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



Folderlocation="C:\\Users\\IgorDC\\Documents\\PdfsToJoin\\"



# nameOfNewFile="NewFileJoined"
# desiredFileType="testFile"


nameOfNewFile="comprovantesResistenciaIgor"
desiredFileType='comprovanteResistencia'

splitSymbol='('



JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType,splitSymbol=splitSymbol)



