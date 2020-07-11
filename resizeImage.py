from PIL import Image



def resizeImage(Location,inputImageName,outputImageName,Imagewidth,Imageheight):
    
    image = Image.open(Location + inputImageName)

    new_image = image.resize((Imagewidth, Imageheight))

    new_image.save(Location + outputImageName)

    print("new image size= ",Imagewidth," x ",Imageheight)

    print("Done Resizing")



# ReferenceValueW=1700
# ReferenceValueH=2200

# multiplicationFactor=ReferenceValueH/ReferenceValueW

# dpi=96

# Imagewidth=int(7.9*dpi)

# Imageheight=int(multiplicationFactor*Imagewidth)


# print('Imagewidth',Imagewidth)


# print('Imageheight',Imageheight)

# inputImageName="WordTojpgFile_1.jpg"

# Location="C:\\Users\\IgorDC\\Desktop\\"





# resizeImage(Location=Location,inputImageName=inputImageName,outputImageName=inputImageName,Imagewidth=Imagewidth,Imageheight=Imageheight)