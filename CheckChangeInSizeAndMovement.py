import CreateBlackCross
import RunImportImageMacro
import excelToJpg

#this program gets an image and an exel file and imports the image into the excel file

def CheckChangeInSizeAndMovement(excelLocation,excelFile,imageLocation,inputImageName,excelIntoImageFileName):

    RunImportImageMacro.RunImportImageMacro(excelLocation=excelLocation,excelFile=excelFile,imageLocation=imageLocation,imageFilename=inputImageName)

    OutputFinalFilename=excelToJpg.excelToJpg(excelFileName=excelFile,FolderLocation=excelLocation,OutputFilename=excelIntoImageFileName)

    return OutputFinalFilename





# imageLocation="C:\\Users\\IgorDC\\Desktop\\"
# excelLocation="C:\\Users\\IgorDC\\Desktop\\"


# imageLocation="C:\\Users\\IgorDC\\Desktop\\JpgImageTest\\"

# excelLocation=imageLocation

# excelFile="MacroTest.xlsx"

# inputImageName='BlackCross.jpg'




# excelIntoImageFileName="BlackCrossCheck.jpg"

# CheckChangeInSizeAndMovement(excelLocation,excelFile,imageLocation,inputImageName,excelIntoImageFileName)