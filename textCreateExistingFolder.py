import os


directoryToCheck = r'C:\Users\Tigereye\Documents\TestExistingDir' + '\\'

try:
    os.mkdir(directoryToCheck)

except:
    pass