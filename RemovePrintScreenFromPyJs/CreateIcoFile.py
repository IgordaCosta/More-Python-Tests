from PIL import Image



def CreateIcoFile(Location, pngFileName,icoFileName):
    png = Image.open(Location + '\\'+ pngFileName)
    png.save(Location + '\\'+ icoFileName, sizes=[(256, 256)])
    ico = Image.open(Location + '\\'+ icoFileName)



Location = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller5\CSSAutoFormFiller\_images'

pngFileName = 'LogInImgBACKUP.png'

icoFileName = 'icon.ico'

CreateIcoFile(Location, pngFileName,icoFileName)