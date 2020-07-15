import CheckChangeInSizeAndMovement
import ComparingImages


def CheckDifferenceInXYImageChange(imageH,ImageW,excelLocation,excelFile,ChangedImageFolder,inputImageLocation,inputImageName,outputImageName,excelIntoImageFileName):

    ChangedImageName=CheckChangeInSizeAndMovement.CheckChangeInSizeAndMovement(excelLocation=excelLocation,excelFile=excelFile,imageLocation=inputImageLocation,inputImageName=inputImageName,excelIntoImageFileName=excelIntoImageFileName)

    ComparingImages.ComparingImages(imageH=imageH,ImageW=ImageW,ChangedImageFolder=ChangedImageFolder,ChangedImageName=ChangedImageName,inputImageLocation=inputImageLocation,inputImageName=inputImageName,outputImageName=outputImageName)






excelLocation="C:\\Users\\IgorDC\\Desktop\\"

inputImageLocation="C:\\Users\\IgorDC\\Desktop\\"

ChangedImageFolder="C:\\Users\\IgorDC\\Desktop\\"
excelFile="MacroTest.xlsx"

inputImageName='BlackCross.jpg'

outputImageName='BlackCross1700x2200.jpg'





excelIntoImageFileName="BlackCrossCheck.jpg"



imageH=980
ImageW=758



CheckDifferenceInXYImageChange(imageH,ImageW,excelLocation,excelFile,ChangedImageFolder,inputImageLocation,inputImageName,outputImageName,excelIntoImageFileName)