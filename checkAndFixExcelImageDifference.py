import shiftImage
import CheckDifferenceInExcelImage


# this program checks the x and y shift when converting an excel file that was created by the program into an image file then fixes this difference
# so the excel file when converting to an image will look the same as of the original excel file

def checkAndFixExcelImageDifference(FolderLocation,excelFileName,OutputImageFilename,imageH,ImageW,inputImageName,outputImageName,shiftImageOutputImageName):

    shiftX, shiftY, OutputFinalFilename, noError = CheckDifferenceInExcelImage.CheckDifferenceInExcelImage(excelFileName=excelFileName,FolderLocation=FolderLocation,OutputFilename=OutputImageFilename,imageH=imageH,ImageW=ImageW,ChangedImageFolder=FolderLocation,inputImageName=inputImageName,outputImageName=outputImageName)

    print(shiftX)

    print('first shiftX above')

    print(shiftY)

    print('first shiftY above')

    if noError:
        if shiftX + shiftY==0:
            print("noImageShiftingNeeded")
        else:
            shiftImage.shiftImage(inputImageFilename=OutputFinalFilename,inputImageFileLocation=FolderLocation,outputImageName=shiftImageOutputImageName,shiftX=shiftX,shiftY=shiftY)

            print("Done check and fix excel image difference")

            print("New difference if bellow")

            shiftX, shiftY, OutputFinalFilename, noError =CheckDifferenceInExcelImage.CheckDifferenceInExcelImage(excelFileName=excelFileName,FolderLocation=FolderLocation,OutputFilename=shiftImageOutputImageName,imageH=imageH,ImageW=ImageW,ChangedImageFolder=FolderLocation,inputImageName=inputImageName,outputImageName=outputImageName, OutputFilenameExcel=False)

            print(shiftX)

            print('last shiftX above')

            print(shiftY)

            print('last shiftY above')
        

    else:
        print("error opening excel file")




FolderLocation="C:\\Users\\IgorDC\\Desktop\\"
excelFileName="MacroTest2.xlsx"
OutputImageFilename="ExcelBlackCrossPaintCheck.jpg"
imageH=980
ImageW=758
inputImageName='BlackCross.jpg'
outputImageName='BlackCross1700x2200.jpg'



shiftImageOutputImageName="ExcelBlackCrossPaintCheckShifted.jpg"




# OutputImageFilename=shiftImageOutputImageName




checkAndFixExcelImageDifference(FolderLocation,excelFileName,OutputImageFilename,imageH,ImageW,inputImageName,outputImageName,shiftImageOutputImageName)