import resizeImage
import getPixelImageSize



def makeTwoImagesSameSize(Location,firstImageFileName,secondImageFileName):

    width, height =getPixelImageSize.getPixelImageSize(Location=Location,filename=firstImageFileName)

    resizeImage.resizeImage(Location=Location,inputImageName=secondImageFileName,outputImageName=secondImageFileName,Imagewidth=width,Imageheight=height)

    print('Images are now same size')



Location="C:\\Users\\IgorDC\\Desktop\\"

firstImageFileName= "emptyExcelJPGFile_1.jpg"   

secondImageFileName="ContractOutput.png"


makeTwoImagesSameSize(Location,firstImageFileName,secondImageFileName)

