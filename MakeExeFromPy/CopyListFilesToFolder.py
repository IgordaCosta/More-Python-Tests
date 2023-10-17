import shutil
import os

def copy_files_to_destination(file_list, destination_folder):
    try:
        # Ensure the destination folder exists; create it if it doesn't
        os.makedirs(destination_folder, exist_ok=True)


        

        for file_path0 in file_list:
            file_path = source_folder + file_path0
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                destination_path = os.path.join(destination_folder, file_name)

                # Copy the file to the destination folder
                shutil.copy2(file_path, destination_path)
                print(f"Copied {file_name} to {destination_folder}")
            else:
                print(f"{file_path} is not a valid file.")

        print("All files copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
source_folder = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesAll' + '\\'
destination_folder = r'C:\Users\Tigereye\Desktop\PythonFilesIntoExes\PythonFilesSelected' + '\\'
file_list = '''
insertIntoDatabase.py, getRealdatafillName.py, placeValuesInFile.py, CloseWorkbook.py, RunDeleteAllTempFilesFromApp.py, FindMyDocumentsDatabasePath.py, CheckJobNameRedo.py, AddToDatabase.py, RemoveCharacters.py, PutListDataIntoImageWithFontSizeStep5.py, AddToable.py, WordOrExcelToPdf.py, copyImageToAppFolder.py, GetAllFontNamesFromFolder.py, ChoosenImageContinue.py, RunDeleteObjFromTableFL.py, JoinImagesIntoPdfSingle.py, GetTitleAndDataForSingleRowTable.py, GetItemAddressAndDescription.py, PlaceAboutImage.py, DeleteFromDataFillName.py, LoadToMultipleFilesDetails.py, getTextfromTxli.py, PutListDataIntoImageWithFontSize.py, CallgetDbData.py, OPFSelectImageFileTitleAndData.py, OpenFolderLocation.py, CreateImageWithMarker.py, ReturnFromSameFileInside.py, GetLocationName.py, IfFirstRun.py, clickedAddFile.py, RemoveLastAndTryAgain.py, JoinPdfWGetDatas.py, LMFAddInfoExcel.py, SortFilesIntoFolders.py, JoinImagesIntoPdfParallel.py, GetDbData.py

'''.strip().split(', ')

copy_files_to_destination(file_list, destination_folder)