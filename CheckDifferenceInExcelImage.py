import ComparingImages
import excelToJpg

# this program turns an excel file with an image back into a pure image file and compares the converted to image file
# to the original image file and finds the x and y difference which will probably exist

def CheckDifferenceInExcelImage(excelFileName,FolderLocation,OutputFilename,imageH,ImageW,ChangedImageFolder,inputImageName,outputImageName, OutputFilenameExcel=True):
    
    if OutputFilenameExcel:
        OutputFinalFilename, noError=excelToJpg.excelToJpg(excelFileName=excelFileName,FolderLocation=FolderLocation,OutputFilename=OutputFilename)
    else:
        OutputFinalFilename=OutputFilename
        noError=True
    
    if noError:
        print("done first function")
        RealXSubtraction, RealYSubtraction=ComparingImages.ComparingImages(imageH=imageH,ImageW=ImageW,ChangedImageFolder=FolderLocation,ChangedImageName=OutputFinalFilename,inputImageLocation=FolderLocation,inputImageName=inputImageName,outputImageName=outputImageName)
    else:
        RealXSubtraction, RealYSubtraction = '', ''
        
    return RealXSubtraction, RealYSubtraction, OutputFinalFilename, noError















# # OutputFilename="ExcelBlackCrossCheck.jpg"


# OutputFilename="ExcelBlackCrossPaintCheck.jpg"

# # excelFileName="CrossExcelJoin.xlsx"

# excelFileName="MacroTest2.xlsx"

# FolderLocation="C:\\Users\\IgorDC\\Desktop\\"
# ChangedImageFolder="C:\\Users\\IgorDC\\Desktop\\"
# inputImageLocation="C:\\Users\\IgorDC\\Desktop\\"
# inputImageName='BlackCross.jpg'
# outputImageName='BlackCross1700x2200.jpg'

# imageH=980
# ImageW=758




# # CheckDifferenceInExcelImage(excelFileName,FolderLocation,OutputFilename,imageH,ImageW,ChangedImageFolder,inputImageLocation,inputImageName,outputImageName)
# RealXSubtraction, RealYSubtraction, OutputFinalFilename, noError=CheckDifferenceInExcelImage(excelFileName,FolderLocation,OutputFilename,imageH,ImageW,ChangedImageFolder,inputImageName,outputImageName)

# print(RealXSubtraction, RealYSubtraction, OutputFinalFilename, noError)