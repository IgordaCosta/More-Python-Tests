import cv2


def MultiplyTextSizeByImageHeight(Location, ImageName = ''):

    imageGotten = cv2.imread(Location + ImageName)

    ImHeight, ImWidth, _ = imageGotten.shape
    # print('width: ', ImWidth)
    # print('height:', ImHeight)

    MuLImageTextSize = round(int(ImHeight)/2200,2)
     
    return MuLImageTextSize




# ImageName = 'temp_A1B1.jpg'

# Location = r'C:\Users\Tigereye\Documents\AutoFormFillerFiles\Temp' +'\\'


# print(MultiplyTextSizeByImageHeight(ImageName, Location))