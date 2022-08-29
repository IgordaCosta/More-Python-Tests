import os
import pathlib

from sqlalchemy import DefaultClause

# print(pathlib.WindowsPath())
print(pathlib.Path.home())    #C:\Users\Tigereye

homedir = pathlib.Path.home()

print(pathlib.WindowsPath.cwd()) # C:\Users\Tigereye\Desktop\Apps\More-Python-Tests



print(homedir.parts) # ('C:\\', 'Users', 'Tigereye')

print(homedir.parts[0]) # C:\

print(homedir.drive) # C:

print(homedir.anchor) #C:\

print(homedir.parent) # C:\Users

print(homedir.name) # Tigereye




#mypath='C:\\Windows\\Fonts\\'

homedir = pathlib.Path.home()

homeanchor = homedir.anchor

WindowsFontsLocation= homeanchor + 'Windows\\Fonts\\'

print(WindowsFontsLocation)




#"C://Windows//Fonts//Arial//arial.ttf"

DefaultFontLocation = WindowsFontsLocation + "Arial\\arial.ttf"

print(DefaultFontLocation)




#Folderlocation="C:\\Users\\IgorDC\\Documents\\AutoFormFillerFiles\\"

homedir = pathlib.Path.home()


Folderlocation = str(homedir) + '\\Documents\\AutoFormFillerFiles\\'

print(Folderlocation)




# Location="C:\\Users\\IgorDC\\Desktop\\"

homedir = pathlib.Path.home()

Location = str(homedir) + '\\Desktop\\'

print(Location)




#location = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles' + '\\'

homedir = pathlib.Path.home()

location = str(homedir) + '\\Documents\\AutoFormFillerOutputFiles\\' 

print(location)



print('done')

