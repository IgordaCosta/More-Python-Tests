import os

def find_matching_items_in_folder(folder_path, input_list):
    matching_items = []
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_name = os.path.splitext(file)[0]
            if file_name in input_list:
                matching_items.append(file_name)
    
    return matching_items

if __name__ == "__main__":
    folder_path = r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated92\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\_engine' + '\\'
    input_list = 'placeValuesInFile.py FindMyDocumentsDatabasePath.py AddToDatabase.py ReturnFromSameFileInside.py DeleteFromDataFillName.py copyImageToAppFolder.py GetDbData.py LoadToMultipleFilesDetails.py LMFAddInfoExcel.py getRealdatafillName.py filenameOPFSelectImageFileTitleAndData.py PutListDataIntoImage.py JoinPdfWGetDatas.py filenamePutListDataIntoImageWithFontSizeStep5.py OpenFolderLocation.py filenameCreateImageWithMarker.py PutListDataIntoImageWithFontSize.py AddToable.py RunDeleteObjFromTableFL.py IfFirstRun.py CloseWorkbook.py filenameRunDeleteAllTempFilesFromApp.py GetLocationName.py CheckJobNameRedo.py insertIntoDatabase.py JoinImagesIntoPdfParallel.py WordOrExcelToPdf.py filenameGetOldStamp.py PlaceAboutImage.py clickedAddFile.py filenameGetItemAddressAndDescription.py filenameGetAllFontNamesFromFolder.py CallgetDbData.py RemoveLastAndTryAgain.py filenameGetTitleAndDataForSingleRowTable.py getFinalLocationItens.py RemoveCharacters.py JoinImagesIntoPdfSingle.py filenameCheckIfLocationWordinDoc.py getTextfromTxli.py filenameCheckJobNameRedo.py'.replace('.py', '').split(' ')
    matching_items = find_matching_items_in_folder(folder_path, input_list)
    
    print("Matching items found in the folder:")
    print(matching_items)
