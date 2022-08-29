import qrcode

import jpgToPdf
# from PIL import Image

# import getTableData



def generateQRfromText(PageNumber, maxPages, NowTimeStamp, TextToAdd, checkContinueValue, SaveLocation, MakePdf = True):

    #str(PageNumber) + '_' +str(maxPages) + '_' +str(NowTimeStamp)


    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )


    # checkContinueValue= 'laksdf1456'        # this data is the check code for the next option

    # TextToAdd = 'Test1023'

    # AllTextToAdd = str(checkContinueValue) +'_' + str(TextToAdd).replace("'", "").replace('"','')


    #number_maxPages_timeStamp_checkValueText_textPassed
    

   
    AllTextToAdd = str(PageNumber) + '_' +str(maxPages) + '_' +str(NowTimeStamp) + '_' + str(checkContinueValue) +'_' + str(TextToAdd).replace("'", "").replace('"','')

    
    print(AllTextToAdd)

    # print('AllTextToAdd above')


    # AllTextToAdd = 'ghkfasdygdi345363_[[bbbaaa1.jpg, aaa1], [bbbnnn1.jpg, nnn1], [bbbmmm1.jpg, mmm1], [bbblll1.jpg, lll1], [bbbrrr1.jpg, rrr1]], [[SaveName, topright]]'    #block after testing   ##### this worked

    #AllTextToAdd = 'ghkfasdygdi345363_[[bbbaaa1.jpg, aaa1]], [[SaveName, topright]]'    #block after testing
    
    
    qr.add_data(str(AllTextToAdd))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # img.save("C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png")

    img.save(SaveLocation)



    if MakePdf:
        SaveLocation2= jpgToPdf.jpgToPdf(ImageName=SaveLocation,ReturnLocation=True)

        return SaveLocation2



    return 'Done'









# TextToAdd = 'this is a third text done now'
# checkContinueValue = 'laksdf1456'
# SaveLocation = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png'


# print(generateQRfromText(TextToAdd, checkContinueValue, SaveLocation))
