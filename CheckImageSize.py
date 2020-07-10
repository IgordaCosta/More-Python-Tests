import CheckIfPixelColorIsBlack
import resizeImage

import imageSizeByMultiplicationValue




InitialValue=7.9

Location= "C:\\Users\\IgorDC\\Desktop\\"

inputImageName="blackTest.png"

# def CheckImageSize(InitialValue,Location,inputImageName,excelImageName,blackShowed=False,Finished=False):
def CheckImageSize(InitialValue,Location,inputImageName,blackShowed=False,Finished=False):

    Imagewidth, Imageheight=imageSizeByMultiplicationValue.imageSizeByMultiplicationValue(MultiplicationValue=InitialValue)

    resizeImage.resizeImage(Location=Location,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)

    ##### here place the allblack image in excel background with a caracter in the upper middle column then
    ##### save excel document and make an image of it

    # IfBlack=CheckIfPixelColorIsBlack.CheckIfPixelColorIsBlack(Location=Location,imageName=excelImageName)
    IfBlack=CheckIfPixelColorIsBlack.CheckIfPixelColorIsBlack(Location=Location,imageName=inputImageName)
    

    if IfBlack==False:
        if blackShowed:
            # InitialValue=InitialValue+0.1
            InitialValue=((InitialValue*10)+1)/10

            Imagewidth, Imageheight=imageSizeByMultiplicationValue.imageSizeByMultiplicationValue(MultiplicationValue=InitialValue)
            resizeImage.resizeImage(Location=Location,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)

            Finished=True
        else:
            # InitialValue=InitialValue+0.1
            InitialValue=((InitialValue*10)+1)/10

            blackShowed=False
            Finished=False
    else:
        # InitialValue=InitialValue-0.1
        InitialValue=((InitialValue*10)-1)/10
        blackShowed=True
        Finished=False

    return InitialValue, blackShowed, Finished




InitialValue, blackShowed, Finished=CheckImageSize(InitialValue,Location,inputImageName)



print(InitialValue, blackShowed, Finished)

print("InitialValue, blackShowed, Finished")



    



