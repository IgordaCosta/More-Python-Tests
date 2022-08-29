import time
import pandas 
import pprint

import pdfToJpg
import getDataFormQRCode




QRPdf = 'C:\\Users\\Tigereye\\Documents\\AutoFormFillerOutputFiles\\Testing\\sample_Joined_1652867195671.pdf' # test location

checkContinueValue = 'ghkfasdygdi345363'

CurrentimeIn = str(int(round(time.time() * 1000)))[-5:]

FolderLocation = '\\'.join(QRPdf.split('\\')[:-1])

filename= QRPdf.split('\\')[-1]

OutputFilename = FolderLocation + filename + '_' + CurrentimeIn + '.jpg'


#QR pdf in images


ImageNames = pdfToJpg.pdfToJpg(PdfFileName=QRPdf, OutputFilename=OutputFilename, diferetiate = False)


#Images get data

TexListGotten = []
for filename in ImageNames:

    decodedText0 = getDataFormQRCode.getDataFormQRCode(filename = filename)
    print(decodedText0)    

    decodedText = decodedText0.split('_',4)

    TexListGotten.append(decodedText)


# images data into pandas dataframe

pprint.pprint(TexListGotten)



# columnsUsed =    ['PageNumber', 'maxPages', 'NowTimeStamp', 'checkContinueValue' ,  'OutputTex' ]
    
# df = pandas.DataFrame(TexListGotten, columns =columnsUsed)


# print(df)

# # print(df['checkContinueValue'][0])


# checkValue = df['checkContinueValue'][0]





# # order pandas datafrome by correct text order

# df.sort_values(by = 'PageNumber' , ascending=False, inplace=True, kind = 'stable')

# # check if text has the starting code proving the data came from the program

# print(df)


# if checkValue == checkContinueValue:
#     print('ok')

# else:
#     print('NOTOKkkkkkkkkkkkkkkkkkkkkkkkkkkkk')



# get all the text parts in the pandas database in the correct order and join in line text



# ### I already got the text and made QR images and joined them into a pdf file
# ### now I have to do the reverse processes
# ### of getting the text from the pdf file QR images