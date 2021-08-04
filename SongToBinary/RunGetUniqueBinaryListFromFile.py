import os

import GetUniqueBinaryListFromFile



numberOfItens = 55

Location = r'C:\Users\IgorDC\Desktop\Apps\More Python Tests\SongToBinary' +'\\'

InputFileLocation = Location + 'video3Sec.mp4'

OutputFileTxtLocation = Location + 'CodesWritten3sVideo55Digit.txt'

LineToGet = 8888


fileTxtInput = OutputFileTxtLocation



GetUniqueBinaryListFromFile.GetUniqueBinaryListFromFile(numberOfItens,InputFileLocation,OutputFileTxtLocation)

GetUniqueBinaryListFromFile.getUniqueValuesFromList(fileTxtInput)

GetUniqueBinaryListFromFile.GetEspecificLineTxt(LineToGet, OutputFileTxtLocation)

os.remove(OutputFileTxtLocation) 

print('Done!')

