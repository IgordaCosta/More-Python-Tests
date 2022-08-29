from audioop import mul
import getTextfromQR
import generateQRfromText



def GetMaxQRCodeLenght():

    NotTopSize = True

    SaveLocation = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png'

    mulVal= 1
    while NotTopSize:
        checkContinueValue = 'ghkfasdygdi345363'
        TextToAdd = ',' * mulVal
        generateQRfromText.generateQRfromText(TextToAdd, checkContinueValue, SaveLocation)

        [TextResult, Passed] = getTextfromQR.getTextfromQR(SaveLocation,checkContinueValue)

        if Passed == 'NotPassed':
            NotTopSize = False
        else:
            mulVal = mulVal + 1
        
    TopTextLenght = len(TextToAdd) + len(checkContinueValue) 
    print(TextResult)

    return TopTextLenght




print(GetMaxQRCodeLenght())    # limit to 50 character lenght

# print(len('ghkfasdygdi345363_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))


