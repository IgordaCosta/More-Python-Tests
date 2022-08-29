from PIL import Image
import time


def ResizeImagesInBulk(ImagesNameLocation):

    AppendedValue = str(int(time.time()*10000000))[-8:]


    #get the lowest dimension to make all even size

    AllYSizeValue = []
    for image in ImagesNameLocation:
        img = Image.open(image)

        (OldX0, CheckedOldY) = img.size

        AllYSizeValue.append(CheckedOldY)



    NewY = min(AllYSizeValue)

    NewImageNameList = []
    for image in ImagesNameLocation:
        img = Image.open(image)

        (OldX, OldY) = img.size

        NewX = int((NewY/OldY)*OldX)

        print(NewX,NewY)


        img.thumbnail((NewX,NewY))

        imageNameOnly = '.'.join(image.split('.')[:-1])

        NewImageName = imageNameOnly + '_RS_' + AppendedValue + '.jpg'

        img.save(NewImageName, optimize=True, quality=40)

        NewImageNameList.append(NewImageName)

    
    return NewImageNameList


# Location = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles' +'\\'

# ImagesNameLocation = [Location + 'A13B1.jpg', Location + 'Testingsample_Joined_1652858852545.pdf_74517_3_RS_53049430.jpg']


# print(ResizeImagesInBulk(ImagesNameLocation))


