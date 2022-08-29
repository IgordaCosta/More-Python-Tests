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








def JoinPdfsFromFileList(FileList,nameOfNewFile):

    pdf2merge =[]
    for filename in FileList:
        if filename.endswith(".pdf"):
            pdf2merge.append(filename)


    if len(pdf2merge)>0:

        # Folderlocation = '\\'.join(pdf2merge[0].split('\\')[:-1])

        # print(pdf2merge)

        pdf2merge.sort()

        # print(pdf2merge)

        pdfWriter = PyPDF2.PdfFileWriter()

        pdfFileObjList = []
        
        for filename in pdf2merge:

            pdfFileObj = open(filename,"rb")
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

            pdfFileObjList.append(pdfFileObj)
        
            for pageNumber in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNumber)
                # print(pageObj)
                pdfWriter.addPage(pageObj)

                # print(pdfWriter)                  
                
                # print(filename+"was appended")

                    
        pdfOutput = open(nameOfNewFile +'.pdf','wb')

        # print(pdfWriter)

        pdfWriter.write(pdfOutput)

        pdfOutput.close()

        for pdfToCLose in pdfFileObjList:
            pdfToCLose.close()
            

        print("Done Join Pdfs")






# Folderlocation="C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\"



# Folderlocation="C:\\Users\\IgorDC\\Documents\\PdfsToJoin\\"



# # nameOfNewFile="NewFileJoined"
# # desiredFileType="testFile"


# nameOfNewFile="comprovantesResistenciaIgor"
# desiredFileType='comprovanteResistencia'

# splitSymbol='('



# JoinPdfs(Folderlocation=Folderlocation,nameOfNewFile=nameOfNewFile,desiredFileType=desiredFileType,splitSymbol=splitSymbol)


# TextCheck = 'tesxtusedtocheckitem'

# print(TextCheck[-5:])

# print(len('daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccx'))