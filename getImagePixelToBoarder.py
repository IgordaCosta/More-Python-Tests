import CheckImageSize


InitialValue=7.9

def getImagePixelToBoarder(InitialValue,Location,inputImageName,excelImageName):
    
    blackShowed=False
    Finished=False

    while Finished==False:
        
        InitialValue, blackShowed, Finished= CheckImageSize.CheckImageSize(InitialValue=InitialValue,Location=Location,inputImageName=inputImageName,excelImageName=excelImageName,blackShowed=blackShowed,Finished=Finished)