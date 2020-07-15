from PIL import Image, ImageDraw




imageH=980
ImageW=758

Location="C:\\Users\\IgorDC\\Desktop\\"
ImageName="BlackBox.jpg"


def CreateBlackBox(ImageW,imageH,Location,ImageName)
    im = Image.new('RGB', (ImageW, imageH), (255, 255, 255))
    draw = ImageDraw.Draw(im)


    draw.rectangle(((ImageW/2)-20, (imageH/2)+20,(ImageW/2)+20 , (imageH/2)-20), fill=(0, 0, 0), outline=None)

    im.save(Location+ImageName, quality=100)

    print("image Created")
