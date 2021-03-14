import os
from hurry.filesize import size
import pandas
import datetime

import DeleteUniqueElements

import pprint
                        
def CheckIfInFilePath(startPath,FileNameCheck, itemToCheck, ExtensionOnly, savePath,MbLowLimit=5,CheckExtension='0', First=1,Second=2,FileNameLongLowerInterVal=-2, FileNameLongHigherInterVal=-1):

    NOerrorGotten = True
    # print('FindAll: ', FindAll)

    startTime = datetime.datetime.now()

    # CheckExtension=str(CheckExtension).lower()
    # total_size = 0
    fileNamePathList = [] 
    fileSizeList = []
    filenameOnlyList = []
    fileNameSizeId  = []
    EasyReadSizeList = []
    dirPathList = []

    FileNameLocationFound = []
    for dirpath, dirnames, filenames in os.walk(startPath+'\\'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                try:
                    
                    
                    # print(fp)
                    # FileNameCheck= True
                    if FileNameCheck:
                        fileNameOnly = fp.split('\\')[-1]
                    else:
                        #checking Directories intead
                        # fileNameOnly = fp.split('\\')[-2:-1]
                        fileNameOnly = fp.split('\\')[FileNameLongLowerInterVal:FileNameLongHigherInterVal]
                        # print(fileNameOnly)

                    
                    

                    # print(fileNameOnly)
                    if FileNameCheck:
                        # if fileNameOnly == 'python.exe':
                        # print('fileNameOnly',fileNameOnly)
                        if ExtensionOnly:
                            ThisFileExtension = '.'+fileNameOnly.split('.')[-1]
                            # print(ThisFileExtension)
                            # print(CheckExtension)
                            if ThisFileExtension.lower() == CheckExtension.lower():
                                FileNameLocationFound.append(fp)
                        else:
                            if fileNameOnly.lower() == itemToCheck.lower():
                                FileNameLocationFound.append(fp)
                    
                    else:
                        if fileNameOnly[0].lower() == itemToCheck.lower():
                            FileNameLocationFound.append(fp)
                        

                    


                    

                    
                    

                except:
                    pass

    print('FileNameLocationFound: ')

    pprint.pprint(FileNameLocationFound)

    pprint.pprint(len(FileNameLocationFound))
    # df = pandas.DataFrame(columns = []) 

    # df['File Directory'] = dirPathList

    # df['File Path'] = fileNamePathList

    # df['Filename Only'] = filenameOnlyList

    # df['File Size'] = fileSizeList

    # df['Easy Read Size'] = EasyReadSizeList

    # df['fileNameSizeId'] = fileNameSizeId

    # if FindAll:

    #     FileteredIndexes = DeleteUniqueElements.ListOfNonUniqueIndexValues(List= fileNameSizeId)  # all same files are discovered

    #     df = df.iloc[FileteredIndexes]

    # #FileteredIndexes = DeleteUniqueElements.ListOfOnlyTwoUniqueValues(List= fileNameSizeId)     #only first two of the same files are discovered

    
    # else:
    #     ListOfUnique, ListOfUniqueCountOrder, ListOfUniqueIndex0 = DeleteUniqueElements.ListSelectedOrderUniqueValues(List= fileNameSizeId)
    #     # print('ListOfUniqueIndex0 bellow')
    #     # print(ListOfUniqueIndex0)
    #     # outputList, ValueGetListChosen
    #     # FilterListFromTwoComparingValues(First,Second,ValueGetList,CheckedList)
    #     FileteredIndexes, OrderValueChosen = DeleteUniqueElements.FilterListFromTwoComparingValues(First=First,Second=Second,ValueGetList=ListOfUniqueCountOrder,CheckedList=ListOfUniqueIndex0)
        
    #     df = df.iloc[FileteredIndexes]

    #     if Second>2: #this is done so the case that only has two qual items is not shown with only one >>> in preference this preference it is not shown since it is looking for a particular case where there are more equal itens
    #         fileNameSizeId2 = list(df['fileNameSizeId'])
    #         ListOfUnique, ListOfUniqueCountOrder, ListOfUniqueIndex2 = DeleteUniqueElements.ListSelectedOrderUniqueValues(List= fileNameSizeId2)
    #     #     FileteredIndexes2, OrderValueChosen = DeleteUniqueElements.FilterListFromTwoComparingValues(First=First,Second=Second,ValueGetList=ListOfUniqueCountOrder,CheckedList=ListOfUniqueIndex)
    #         OrderValueChosen = []
    #         # print(ListOfUniqueCountOrder)
    #         for i in range(len(ListOfUniqueCountOrder)):
    #             print(ListOfUniqueCountOrder[i])
    #             # print(ListOfUniqueCountOrder[i])
    #             if ListOfUniqueCountOrder[i] == 1:
    #                 OrderValueChosen.append(First)
    #             elif ListOfUniqueCountOrder[i] == 2:
    #                 OrderValueChosen.append(Second)
    #             else:
    #                 NOerrorGotten=False   
    #                 print("More then one value appeared for each, it should appear just two") 


    #         df = df.iloc[ListOfUniqueIndex2]
        
    #     if NOerrorGotten:
    #         df['Pairs Chosen'] = OrderValueChosen

    # if NOerrorGotten:

    #     df.sort_values(by='File Size', ascending=False, inplace=True)

    #     df.to_csv(savePath)

    #     print("Done!")

    #     endTime = datetime.datetime.now()

    #     print("amount of time taken to complete: ", str(endTime - startTime))
            

    #     # return size(total_size), total_size


#C:\

# startPath = r'C:\Program Files\LibreOffice'

# startPath = r'C:\ProgramData\Anaconda3'

savePath = r'C:\Users\IgorDC\Desktop\FileSizes\PandasFilesizeDriveC.csv'

startPath = r'C:\Program Files\Microsoft Office\root\Office16'

MbLowLimit = 5

CheckExtension = '.exe'

First = 1

Second = 2

FileNameCheck = True

ExtensionOnly = True

itemToCheck = 'difflib.py'

FileNameLongLowerInterVal=-3

FileNameLongHigherInterVal=-2

# getDirSize(startPath,savePath,MbLowLimit,CheckExtension)

# getDirSize(startPath,savePath,MbLowLimit)

# print(get_size(start_path))
CheckIfInFilePath(startPath,FileNameCheck, itemToCheck, ExtensionOnly, savePath,MbLowLimit,CheckExtension, First,Second,FileNameLongLowerInterVal, FileNameLongHigherInterVal)
# getDirSize(startPath=startPath,savePath=savePath,MbLowLimit=MbLowLimit,First=First,Second=Second)