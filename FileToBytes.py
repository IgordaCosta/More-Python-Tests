import copyFile
import os

import base64
import io
import openpyxl

def getBytesFromFile(filename,Location):  
    # return open(Location+filename, "rb").read() 

    newExtension=".txt"

    filenamebackup=copyFile.copyFile(Location=Location,filename=filename)



    extension=filename.split(".")[-1]

    fileNameWithOldExtesion = filenamebackup + "."+extension



    changeFileExtension(fileNameWithOldExtesion=fileNameWithOldExtesion,newExtension=newExtension,Location=Location)

    

    remove=filename.split(".")[-1]
    filename2=filename.strip("."+remove)

    os.rename(Location+filenamebackup+newExtension,Location+filename2+newExtension)



    data = open(Location+filename2+newExtension, "r", encoding= 'windows-1252').read()
    encoded = base64.b64encode(data) 
    
    return encoded

def createTextFileAndWritre(Location,fileToCreate,data):

    file = open(Location+fileToCreate, "w") 
    file.write(str(data)) 
    file.close() 


def MakeTextFileFromAnother(Datafilename,fileToCreate,Location):

    data=getBytesFromFile(filename=Datafilename,Location=Location)

    createTextFileAndWritre(Location=Location,fileToCreate=fileToCreate,data=data)

    print("Done")

def changeFileExtension(fileNameWithOldExtesion,newExtension,Location):
    
    pre, ext = os.path.splitext(Location+fileNameWithOldExtesion)
    os.rename(Location+fileNameWithOldExtesion, pre + newExtension)


def MakePyFileFromAnother(Datafilename,fileToCreate,Location):

    MakeTextFileFromAnother(Datafilename=Datafilename,fileToCreate=fileToCreate,Location=Location)

    newExtension=".py"

    changeFileExtension(fileNameWithOldExtesion=fileToCreate,newExtension=newExtension,Location=Location)

    print("Done")

def createExcelFileFromByteArray(Location,inputFileName,outputFileName):

    newExtension=".txt"

    changeFileExtension(fileNameWithOldExtesion=inputFileName,newExtension=newExtension,Location=Location)


    remove=inputFileName.split(".")[-1]
    inputFileName=inputFileName.strip("."+remove)

    # f=open(Location + inputFileName + newExtension, "r")
    # if f.mode == 'r':
    #     contents =f.read()

    data = open(Location + inputFileName + newExtension, "r").read()
    decoded = base64.b64decode(data)


    createTextFileAndWritre(Location=Location,fileToCreate=outputFileName,data=decoded)


    fileNameWithOldExtesion=outputFileName

    newExtension="."+remove

    changeFileExtension(fileNameWithOldExtesion=fileNameWithOldExtesion,newExtension=newExtension,Location=Location)



    # f = open(Location+outputFileName, 'wb')
    # # binaryFormat = bytearray(contents,'utf-8')
    # f.write(decoded) #TypeError: a bytes-like object is required, not 'str' 
    # f.close()




    





Datafilename="testPicTOExcelNeedsImprovement.xlsx"
fileToCreate="testPicTOExcelNeedsImprovement.txt"
Location="C:\\Users\\IgorDC\\Desktop\\"

newExtension=".py"


inputFileName="testPicTOExcelNeedsImprovement.py"
outputFileName='OutputTest.xlsx'


# MakeTextFileFromAnother(Datafilename=Datafilename,fileToCreate=fileToCreate,Location=Location)

# changeFileExtension(fileNameWithOldExtesion=fileToCreate,newExtension=newExtension,Location=Location)


MakePyFileFromAnother(Datafilename=Datafilename,fileToCreate=fileToCreate,Location=Location)

# createExcelFileFromByteArray(Location=Location,inputFileName=inputFileName,outputFileName=outputFileName)




