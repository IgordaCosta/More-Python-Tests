from PIL import Image, ImageFile




def makeAllButBlackTransparent(Folder,InputImageName,OutputImageName):

    ImageFile.MAXBLOCK = 2**20

    img = Image.open(Folder+InputImageName)
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            (a, b, c, d)= pixdata[x, y]
            if a>70 and b >70 and c >70:
                pixdata[x, y] = (255, 255, 255, 0)
            # if pixdata[x, y] != (0, 0, 0, 255):
            #     pixdata[x, y] = (255, 255, 255, 0)

    img.save(Folder+OutputImageName, "PNG")

    print("done")


Folder="C:\\Users\\IgorDC\\Desktop\\"
InputImageName="Contract-page-001.jpg"
OutputImageName='ContractOutput.png'


makeAllButBlackTransparent(Folder=Folder,InputImageName=InputImageName,OutputImageName=OutputImageName)




# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)