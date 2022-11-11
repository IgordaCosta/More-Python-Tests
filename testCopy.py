import shutil
import re



# string = "C:\\Windows\Users\alexb"

# raw_string = r"{}".format(string)

# BaseFileLocation2 = 'C:\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela.jpg'

# BaseFileLocation = 'C:\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela__aa9f70e1c3b282_temp.jpg'






# BaseFileLocation = r"{}".format('C:\Users\Tigereye\Documents\AutoFormFillerFiles\adosMultaFacesIsabela__aa9f70e1c3b282_temp.jpg')




BaseFileLocation2 = 'C:/Users/Tigereye/Documents/AutoFormFillerFiles/adosMultaFacesIsabela.jpg'
BaseFileLocation =  'C:/Users/Tigereye/Documents/AutoFormFillerFiles/adosMultaFacesIsabela__f4eb74ae03b282_temp.jpg'





shutil.copy(BaseFileLocation2, BaseFileLocation)

