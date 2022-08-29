from distutils import extension
import cv2

import pdfToJpg



# location = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles' +'\\'

# filename = 'img13-2022-01-20_23-13-25_QR.png'

def getDataFormQRCode(filename, location=''):

    extensionUsed = filename.split('.')[-1]

    # print(filename)

    # print('filename start above')
    
    if extensionUsed == 'pdf':
        # print('is pdf')
        pdfToJpg.pdfToJpg(PdfFileName=filename, OutputFilename=filename)

        # print(filename)

        # print('filename mid above')

        filename2 =  '.'.join(filename.split('.')[:-1]) + '.jpg'

        # print(filename2)

        # print('filename2 above')

    else:
        filename2 = filename

    
        
    Wholefilename = location + filename2

    # print(Wholefilename)

    # print('Wholefilename above')
      
    image = cv2.imread(Wholefilename)
        
    qrCodeDetector = cv2.QRCodeDetector()
        
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

    return decodedText




# import win32com
# print(win32com.__gen_path__)




# ListOfLocations = ['C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample_0.png', 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample_36.png', 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\sample_81.png']



# ListOfLocations = ['C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample_01652867195671.png', 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample_131652867195671.png', 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample_151652867195671.png', 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample_521652867195671.png']

# print(getDataFormQRCode(filename = ListOfLocations[4]))

# # print('_______________________________________________________________')

# # print(string.printable)

# # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')


# # import string
# # textoAdd2 = string.printable

# # letterID = 4

# # ItemStep = 0

# # ItemToAdd = textoAdd2[ItemStep:letterID+1]

# # print(ItemToAdd)


# item = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles\Testing\sample_Joined_1652867195671.pdf'

# print(item.split('.')[-1])