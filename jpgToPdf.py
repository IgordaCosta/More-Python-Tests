from PIL import Image


def jpgToPdf(Folderlocation, ImageName,PdfSaveName):

    image1 = Image.open(Folderlocation + ImageName)
    im1 = image1.convert('RGB')
    im1.save(Folderlocation + PdfSaveName)



Folderlocation="C:\\Users\\IgorDC\\Documents\\PdfsToJoin\\"

ImageName = 'comprovanteResistencia2.jpg'

PdfSaveName = 'comprovanteResistencia2.pdf'



jpgToPdf(Folderlocation, ImageName,PdfSaveName)