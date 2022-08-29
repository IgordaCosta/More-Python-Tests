from googletrans import Translator, constants
from pprint import pprint

# import googletrans

with open('C:/Users/Tigereye/Downloads/aquaman.(2018).eng.1cd.(7900850)/Aquaman.2018.2160p.UHD.BluRay.X265.10bit.HDR.TrueHD.7.1.Atmo.srt',  encoding="utf8") as f:
    lines = f.read().splitlines()


# print(lines)

start=True
Allitems = []

r=0
Allitems.append([])

for i in range(len(lines)):
    
    if lines[i] == '':
        # print('is empty')
        Allitems.append([])
        Allitems[r].append(lines[i])
        r=r+1
        
      
    else:
        # print('not empty')
        Allitems[r].append(lines[i])



# print(Allitems)
   


print(Allitems[0])

print(Allitems[0][1])



# translator = Translator()



# translation = translator.translate("Hola Mundo", dest="ar")



# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
