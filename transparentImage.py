from PIL import Image, ImageFile




def whiteIntoTrasparent(Folder,InputImageName,OutputImageName):

    ImageFile.MAXBLOCK = 2**20

    img = Image.open(Folder+InputImageName)
    img = img.convert("RGBA")

    pixdata = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (255, 255, 255, 255):
                pixdata[x, y] = (255, 255, 255, 0)

    img.save(Folder+OutputImageName, "PNG")

    print("done")


Folder="C:\\Users\\IgorDC\\Desktop\\"
InputImageName="Contract-page-001.jpg"
OutputImageName='ContractOutput.png'


whiteIntoTrasparent(Folder=Folder,InputImageName=InputImageName,OutputImageName=OutputImageName)




# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)