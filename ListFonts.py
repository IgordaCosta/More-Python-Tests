import os
from os import listdir

from fontTools import ttLib

# import path

import pathlib
from os.path import isfile, join




mypath='C:\\Windows\\Fonts\\'


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]



# print(onlyfiles)


# print('onlyfiles above')


OnlyttfFiles=[f.replace("."+f.split(".")[-1],'') for f in onlyfiles if (f.split(".")[-1]=="ttf")]



# print(OnlyttfFiles) ####### save this for later


# print(len(OnlyttfFiles))

# print('len(OnlyttfFiles)')


# print('OnlyttfFiles above')


allPathsList = []

for folder, subs, files in os.walk(mypath):
  for filename in files:
      if (filename.split(".")[-1]=="ttf"):
        allPathsList.append(os.path.abspath(os.path.join(folder, filename)))



print(allPathsList)

# print(len(allPathsList))

# print('len(allPathsList)')


