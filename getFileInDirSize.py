import os
from hurry.filesize import size
import pandas
import datetime

import DeleteUniqueElements

def getDirSize(startPath,savePath,MbLowLimit=5,CheckExtension='0',FindAll=False, First=1,Second=2):

    NOerrorGotten = True
    # print('FindAll: ', FindAll)

    startTime = datetime.datetime.now()

    CheckExtension=str(CheckExtension).lower()
    # total_size = 0
    fileNamePathList = [] 
    fileSizeList = []
    filenameOnlyList = []
    fileNameSizeId  = []
    EasyReadSizeList = []
    dirPathList = []
    for dirpath, dirnames, filenames in os.walk(startPath+'\\'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
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

                            fileNameSizeId.append(str(sizeFile)+'_'+str(LastModifiedTime)+'_'+filenameOnly)
                        
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


                    else:

                        pass
                    

                except:
                    pass

    df = pandas.DataFrame(columns = []) 

    df['File Directory'] = dirPathList

    df['File Path'] = fileNamePathList

    df['Filename Only'] = filenameOnlyList

    df['File Size'] = fileSizeList

    df['Easy Read Size'] = EasyReadSizeList

    df['fileNameSizeId'] = fileNameSizeId

    if FindAll:

        FileteredIndexes = DeleteUniqueElements.ListOfNonUniqueIndexValues(List= fileNameSizeId)  # all same files are discovered

        df = df.iloc[FileteredIndexes]

    #FileteredIndexes = DeleteUniqueElements.ListOfOnlyTwoUniqueValues(List= fileNameSizeId)     #only first two of the same files are discovered

    
    else:
        ListOfUnique, ListOfUniqueCountOrder, ListOfUniqueIndex0 = DeleteUniqueElements.ListSelectedOrderUniqueValues(List= fileNameSizeId)
        # print('ListOfUniqueIndex0 bellow')
        # print(ListOfUniqueIndex0)
        # outputList, ValueGetListChosen
        # FilterListFromTwoComparingValues(First,Second,ValueGetList,CheckedList)
        FileteredIndexes, OrderValueChosen = DeleteUniqueElements.FilterListFromTwoComparingValues(First=First,Second=Second,ValueGetList=ListOfUniqueCountOrder,CheckedList=ListOfUniqueIndex0)
        
        df = df.iloc[FileteredIndexes]

        if Second>2: #this is done so the case that only has two qual items is not shown with only one >>> in preference this preference it is not shown since it is looking for a particular case where there are more equal itens
            fileNameSizeId2 = list(df['fileNameSizeId'])
            ListOfUnique, ListOfUniqueCountOrder, ListOfUniqueIndex2 = DeleteUniqueElements.ListSelectedOrderUniqueValues(List= fileNameSizeId2)
        #     FileteredIndexes2, OrderValueChosen = DeleteUniqueElements.FilterListFromTwoComparingValues(First=First,Second=Second,ValueGetList=ListOfUniqueCountOrder,CheckedList=ListOfUniqueIndex)
            OrderValueChosen = []
            # print(ListOfUniqueCountOrder)
            for i in range(len(ListOfUniqueCountOrder)):
                print(ListOfUniqueCountOrder[i])
                # print(ListOfUniqueCountOrder[i])
                if ListOfUniqueCountOrder[i] == 1:
                    OrderValueChosen.append(First)
                elif ListOfUniqueCountOrder[i] == 2:
                    OrderValueChosen.append(Second)
                else:
                    NOerrorGotten=False   
                    print("More then one value appeared for each, it should appear just two") 


            df = df.iloc[ListOfUniqueIndex2]
        
        if NOerrorGotten:
            df['Pairs Chosen'] = OrderValueChosen

    if NOerrorGotten:

        df.sort_values(by='File Size', ascending=False, inplace=True)

        df.to_csv(savePath)

        print("Done!")

        endTime = datetime.datetime.now()

        print("amount of time taken to complete: ", str(endTime - startTime))
            

        # return size(total_size), total_size


#C:\

startPath = 'C:\\'

savePath = r'C:\Users\IgorDC\Desktop\FileSizes\PandasFilesizeDriveC.csv'

MbLowLimit = 5

CheckExtension = '.Exe'

First = 1

Second = 2

# getDirSize(startPath,savePath,MbLowLimit,CheckExtension)

# getDirSize(startPath,savePath,MbLowLimit)

# print(get_size(start_path))

getDirSize(startPath=startPath,savePath=savePath,MbLowLimit=MbLowLimit,First=First,Second=Second)