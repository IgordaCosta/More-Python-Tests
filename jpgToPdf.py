from PIL import Image


def jpgToPdf(ImageName,Folderlocation ='', PdfSaveName='', ReturnLocation = False):

    image1 = Image.open(Folderlocation + ImageName)
    im1 = image1.convert('RGB')

    if PdfSaveName == '':

        PdfSaveName = '.'.join(ImageName.split('.')[:-1]) + '.pdf'

    SaveLocation = Folderlocation + PdfSaveName
    
    im1.save(SaveLocation)

    if ReturnLocation:
        
        return SaveLocation



# Folderlocation="C:\\Users\\IgorDC\\Documents\\PdfsToJoin\\"

# ImageName = 'comprovanteResistencia2.jpg'

# PdfSaveName = 'comprovanteResistencia2.pdf'



# jpgToPdf(Folderlocation, ImageName,PdfSaveName)



