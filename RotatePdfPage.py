import PyPDF2


def RotePdfPage(Folderlocation, PdfFileName):

    pdf_in = open(Folderlocation + PdfFileName, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()

    for pagenum in range(pdf_reader.numPages):
        page = pdf_reader.getPage(pagenum)
        page.rotateClockwise(90)
        pdf_writer.addPage(page)

    pdf_out = open(Folderlocation + PdfFileName, 'wb')
    pdf_writer.write(pdf_out)
    pdf_out.close()
    pdf_in.close()





Folderlocation="C:\\Users\\IgorDC\\Documents\\PdfsToJoin\\ContradoDeAluguelIgor\\"


PdfFileName = '9-16-21 6-11 PM(2).pdf'




RotePdfPage(Folderlocation, PdfFileName)

print("Done")