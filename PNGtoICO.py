from PIL import Image
# filename = r'logo.png'


Location = r'C:\Users\Tigereye\Desktop\ToICO' + '\\'
fileUsed = 'LogInImg.png'
fileUsed2 = 'NEWLogInImg.ico'

filename = Location + fileUsed

img = Image.open(filename)

filename2 = Location + fileUsed2

# img.save('logo.ico')

# ====================

# Optionally, you may specify the icon sizes you want:

icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
img.save(filename2, sizes=icon_sizes)


print('DONE')