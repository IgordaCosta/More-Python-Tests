import os
from hurry.filesize import size
import pandas
import datetime

import GetUniqueValuesInList

def getDirSize(startPath1, startPath2 ,savePath,MbLowLimit=5,CheckExtension='0',FindAll=False, First=1,Second=2):

    NOerrorGotten = True
    # print('FindAll: ', FindAll)

    startTime = datetime.datetime.now()

    CheckExtension=str(CheckExtension).lower()
    # total_size = 0
   

    StartLocations = [startPath1, startPath2]


    fileNamePathList = [] 
    fileSizeList = []
    filenameOnlyList = []
    fileNameSizeId  = []
    EasyReadSizeList = []
    dirPathList = []
    startPathStepList = []

    for startPathStep in range(len(StartLocations)):

        startPath =StartLocations[startPathStep]

        # print(startPath)

        # print(startPathStep)


        for dirpath, dirnames, filenames in os.walk(startPath+'\\'):
            for f in filenames:
                fp = os.path.join(dirpath, f)

                # print(fp)

                relativeLocationPath = fp.split(startPath)[-1]

                # print(relativeLocationPath)

                # skip if it is symbolic link

                if not os.path.islink(fp):
                    try:
                        
                        sizeFile=os.path.getsize(fp)

                        if sizeFile>(1024*1024*MbLowLimit):

                            if CheckExtension == '0':

                                filenameOnly=fp.split('\\')[-1]
                                dirPathList.append(dirpath)
                                fileNamePathList.append(fp)
                                filenameOnlyList.append(filenameOnly)
                                fileSizeList.append(sizeFile)

                                EasyReadSizeList.append(size(sizeFile))

                                LastModifiedTime = os.path.getmtime(fp)

                                fileNameSizeId.append(str(sizeFile)+'_'+str(LastModifiedTime)+'_'+relativeLocationPath)

                                startPathStepList.append(startPathStep)
                            
                            else:
                                filenameOnly=fp.split('\\')[-1]

                                FileExtenstion='.'+filenameOnly.split('.')[-1]

                                FileExtenstion=FileExtenstion.lower()


                                if FileExtenstion == CheckExtension:
                                    dirPathList.append(dirpath)
                                    fileNamePathList.append(fp)
                                    filenameOnlyList.append(filenameOnly)
                                    fileSizeList.append(sizeFile)

                                    EasyReadSizeList.append(size(sizeFile))

                                    LastModifiedTime = os.path.getmtime(fp)

                                    fileNameSizeId.append(str(sizeFile)+'_'+str(LastModifiedTime)+'_'+filenameOnly)

                                    startPathStepList.append(startPathStep)


                        else:

                            pass
                        

                    except:
                        pass


        

            
        # print(dirPathList)

        # print(fileNamePathList)

        # print(filenameOnlyList)

        # print(fileSizeList)

        # print(EasyReadSizeList)

        # print(fileNameSizeId)




    df = pandas.DataFrame(columns = []) 

    df['File Directory'] = dirPathList

    df['File Path'] = fileNamePathList

    df['Filename Only'] = filenameOnlyList

    df['File Size'] = fileSizeList

    df['Easy Read Size'] = EasyReadSizeList

    df['fileNameSizeId'] = fileNameSizeId

    df['startPathStep'] = startPathStepList


    UniqueDataFilter = GetUniqueValuesInList.GetUniqueValuesInList(List = fileNameSizeId )
    
    # print(UniqueDataFilter)

    df = df[UniqueDataFilter]

        

   
        

    if NOerrorGotten:

        df.sort_values(by='File Size', ascending=False, inplace=True)

        df.to_csv(savePath)

        print("Done!")

        endTime = datetime.datetime.now()

        print("amount of time taken to complete: ", str(endTime - startTime))
            

        # return size(total_size), total_size


#C:\

# startPath = 'C:\\'

# startPath = r'C:\Users\IgorDC\Downloads' +'\\'



savePath = r'C:\Users\IgorDC\Desktop\FileSizes\PandasFilesizeDriveC.csv'

MbLowLimit = 0

CheckExtension = '.Exe'

First = 1

Second = 2

startPath1 = r'C:\Users\IgorDC\Downloads\fontawesome-free-5.14.0-web' +'\\'

startPath2 = r'C:\Users\IgorDC\Desktop\fontawesome-free-5.14.0-web' +'\\'

# getDirSize(startPath,savePath,MbLowLimit,CheckExtension)

# getDirSize(startPath,savePath,MbLowLimit)

# print(get_size(start_path))

getDirSize(startPath1 = startPath1, startPath2 = startPath2 ,savePath=savePath,MbLowLimit=MbLowLimit,First=First,Second=Second)