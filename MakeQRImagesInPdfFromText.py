import os
import time


import generateQRfromText
import getDataFormQRCode
import jpgToPdf
import JoinPdfs


#textoAdd = 'daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccx'



import string

# # print(string.ascii_lowercase + string.ascii_uppercase + string.digits)

# print(string.printable)

textoAdd = string.ascii_lowercase + string.ascii_uppercase + string.digits

# textoAdd = string.printable


letterID = 0

checkContinueValue0 = 'ghkfasdygdi345363'


SaveLocation = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample' # test location


extension = '.png'





# print(len(ItemToAdd))




Currentime = str(int(round(time.time() * 1000)))

CurrentimeIn = str(int(round(time.time() * 1000)))[-5:]

NowTimeStamp = CurrentimeIn

ImageIDNameUsed = ''
NewImage = True
ItemStep = 0
ImageMadeList = []

NumberOfItens = len(textoAdd)

# for letterID in range(NumberOfItens):

NotFinished = True


checkContinueValue = checkContinueValue0




while NotFinished:


    print(ItemStep)

    print('ItemStep above++')

    print(letterID)

    print('letterID above++')


    
    if ItemStep == 0:
        ItemToAdd = textoAdd[ItemStep:letterID+1]
    else:
        ItemToAdd = textoAdd[ItemStep+1:letterID+1]

    # print(ItemToAdd)

    # checkContinueValue = checkContinueValue0

    if NewImage:

        ItemStepOld = ItemStep

        # ItemStep = letterID

        NewImage = False
        ImageIDNameUsed =  str(ItemStep) + Currentime


        filename =  SaveLocation + '_'+ ImageIDNameUsed+ extension


        print(ItemToAdd)

        print("item to add after new image abv")


        

        if ItemStep == 0:
            # generateQRfromText(PageNumber, maxPages, NowTimeStamp, TextToAdd, checkContinueValue, SaveLocation)
            print('gen1')
            filename3 = generateQRfromText.generateQRfromText(PageNumber=letterID, maxPages= NumberOfItens, NowTimeStamp=NowTimeStamp, checkContinueValue = checkContinueValue, TextToAdd=ItemToAdd, SaveLocation= filename)
        else:
            checkContinueValue = 'X'
            print('gen2')
            filename3 = generateQRfromText.generateQRfromText(PageNumber=letterID, maxPages= NumberOfItens, NowTimeStamp=NowTimeStamp, checkContinueValue = checkContinueValue, TextToAdd=ItemToAdd, SaveLocation= filename)

        # ImageMadeList.append(filename)


    else:
        
        # if str(ItemStep ) == '0':
        #     checkContinueValue = checkContinueValue0

        # else:
        
        #     # checkContinueValue = 'X'

        # ItemToAdd = textoAdd[ItemStep+1:letterID+1]
        #     pass

        

        if ItemStep == 0:
            checkContinueValue = checkContinueValue0
        else:
            checkContinueValue = 'X'


        print('gen3')
        filename3 = generateQRfromText.generateQRfromText(PageNumber=letterID, maxPages= NumberOfItens, NowTimeStamp=NowTimeStamp, checkContinueValue = checkContinueValue, TextToAdd=ItemToAdd, SaveLocation= filename)


    # textGotten = getDataFormQRCode.getDataFormQRCode(filename=filename)
    textGotten = getDataFormQRCode.getDataFormQRCode(filename=filename3)
    

    # print('_'+textGotten + '_')

    if textGotten == '':
        NewImage = True

        print(checkContinueValue)

        print('checkContinueValue above')

        letterID = letterID -1
        # ItemToAdd = textoAdd[ItemStepOld:letterID+1]

        print('CHECKVALUENOW++++++++++++++++++++++++++++++++++++++++++++')
        
        if ItemStepOld == 0:

            checkContinueValue = checkContinueValue0
            
            ItemToAdd = textoAdd[ItemStep:letterID+1]

        else:  

            checkContinueValue = 'X'

            ItemToAdd = textoAdd[ItemStep+1:letterID+1]


        ImageIDNameUsed =  str(ItemStep) + Currentime

        # print('REALTEXT added bellow')

        # print(ItemToAdd)

        # print('REALTEXT added above')

        print('gen4')
        # filename =  SaveLocation + '_'+ ImageIDNameUsed+ extension
        filename3 = generateQRfromText.generateQRfromText(PageNumber=letterID, maxPages= NumberOfItens, NowTimeStamp=NowTimeStamp, checkContinueValue = checkContinueValue, TextToAdd=ItemToAdd, SaveLocation= filename)
        ImageMadeList.append(filename)


        # if ItemStepOld == 0:
        #     checkContinueValue = 'X'


        
        # ItemStep = ItemStep + 1

        ItemStep = letterID

        letterID = letterID + 1
        
    else:
        letterID = letterID + 1

        if NumberOfItens == letterID:

            ItemToAdd = textoAdd[ItemStep+1:]
            ImageIDNameUsed =  str(ItemStep) + Currentime

            print('gen5')
            # filename =  SaveLocation + '_'+ ImageIDNameUsed+ extension
            filename3 = generateQRfromText.generateQRfromText(PageNumber=letterID, maxPages= NumberOfItens, NowTimeStamp=NowTimeStamp, checkContinueValue = checkContinueValue, TextToAdd=ItemToAdd, SaveLocation= filename)
            ImageMadeList.append(filename)

            NotFinished = False
    

print(ImageMadeList)

NewPdfLocationList = []
for ImageName in ImageMadeList:

    SaveLocaion = jpgToPdf.jpgToPdf(ImageName,Folderlocation ='', PdfSaveName='', ReturnLocation = True)

    NewPdfLocationList.append(SaveLocaion)


print(NewPdfLocationList)


ImageIDNameUsed2 = 'Joined_'  + Currentime

filename2 =  SaveLocation + '_'+ ImageIDNameUsed2

JoinPdfs.JoinPdfsFromFileList(FileList=NewPdfLocationList,nameOfNewFile=filename2)

# for ImageRm in ImageMadeList:
#     os.remove(ImageRm)


for pdfRm in NewPdfLocationList:
    os.remove(pdfRm)

print(filename2)

### below I will join the images into a pdf file
### afterwards I have to do the reverse processes
### of getting the text from the pdf file