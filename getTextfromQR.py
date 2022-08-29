import cv2 as cv



def getTextfromQR(SaveLocation,checkContinueValue):

    # checkContinueValue= 'laksdf1456'  

    # im = cv.imread("C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png")

    im = cv.imread(SaveLocation)


    det = cv.QRCodeDetector()

    retval, points, straight_qrcode = det.detectAndDecode(im)

    print(retval)


    # print(retval.split('_')[0])

    checkvalue = retval.split('_')[0]

    Passed = 'NotPassed'

    if checkvalue == checkContinueValue:
        Passed = 'CheckPassed'
        TextResult = retval.split('_')[1]

    else:
        TextResult = ''


    # print(TextResult)

    return [TextResult, Passed]




# # checkContinueValue= 'laksdf1456'      

# checkContinueValue = 'ghkfasdygdi345363'

# # SaveLocation = "C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png"


# # SaveLocation = "C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\img3-2021-12-30 21-57-22_QR.png"

# SaveLocation = "C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\img13-2022-01-20_21-58-33_QR.png"

# # img3-2021-12-30 20-41-10_QR.png
# # SaveLocation = "C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\img3-2021-12-30 19-42-16_QR.png"

# SaveLocation = "C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\img2-2022-04-23_20-58-52_QR.png"

# SaveLocation = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample.png'


# print(getTextfromQR(SaveLocation,checkContinueValue))

