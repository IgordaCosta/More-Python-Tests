import glob
import os

def compile_python_scripts_to_exe_files(LocationPy, python_scripts ):
    """Compiles all Python scripts in the current directory to exe files using PyInstaller."""

    os.chdir(LocationPy)
  # Get all Python scripts in the current directory.


    # Compile each Python script to an exe file.
  
    pyinstaller_command = f'pyinstaller --onefile {python_scripts}'
    os.system(pyinstaller_command)



# LocationPy= r'C:\Users\Tigereye\Desktop\Apps\CSSAutoFormFiller7_Updated92\CSSAutoFormFiller7_Presentable\CSSAutoFormFiller\_engine' + '\\'

LocationPy= r'E:\Apps\CSSAutoFormFiller7_Updated93\CSSAutoFormFiller\_engine' + '\\'

# python_scripts= 'AddToable.py AddToable.py AddToDatabase.py CallgetDbData.py CheckJobNameRedo.py clickedAddFile.py clickedAddFile.py CloseWorkbook.py copyImageToAppFolder.py DeleteFromDataFillName.py FindMyDocumentsDatabasePath.py GetDbData.py getFinalLocationItens.py GetLocationName.py getRealdatafillName.py getTextfromTxli.py IfFirstRun.py insertIntoDatabase.py JoinImagesIntoPdfParallel.py JoinImagesIntoPdfSingle.py JoinPdfWGetDatas.py LMFAddInfoExcel.py IfFirstRun.py insertIntoDatabase.py JoinImagesIntoPdfParallel.py JoinImagesIntoPdfSingle.py JoinPdfWGetDatas.py LMFAddInfoExcel.py LoadToMultipleFilesDetails.py OpenFolderLocation.py PlaceAboutImage.py placeValuesInFile.py placeValuesInFile.py PutListDataIntoImage.py PutListDataIntoImageWithFontSize.py RemoveCharacters.py RemoveLastAndTryAgain.py ReturnFromSameFileInside.py RunDeleteObjFromTableFL.py WordOrExcelToPdf.py'.split(' ')

python_scripts= 'AddToDatabase.py'

compile_python_scripts_to_exe_files(LocationPy, python_scripts)