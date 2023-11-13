import os
import shutil
import subprocess



def MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination):
    PathToUseSource = os.path.join(target_dir, LocationUsedSource)
    PathToUseDestination = os.path.join(target_dir,LocationUsedDestination,LocationUsedSource) 

    try:
        os.mkdir(PathToUseDestination)
    except:
        pass

    try:
        shutil.copytree(PathToUseSource, PathToUseDestination)
    except:
        pass

    try:
        shutil.rmtree(PathToUseSource)
    except:
        pass




# Set the source and target directories
source_dir = r'F:\Stuff\PythonFilesIntoExes\A_SourceOfPythonForExes' + '\\'
target_dir = r'F:\Stuff\PythonFilesIntoExes\A_OutputExeLocation' + '\\'

# # Ensure the target directory exists, or create it
# if not os.path.exists(target_dir):
#     os.makedirs(target_dir)

# # Directory with Python files to be converted
source2_dir = r'F:\Stuff\PythonFilesIntoExes\A_GuideToExeOutput'

# Get a list of files in the source2 directory to be converted
files_to_convert = [filename for filename in os.listdir(source2_dir) if filename.endswith(".py")]

# Iterate through the specified Python files and convert them
FileLocation = 0
numberOfFilesToConvert = len(files_to_convert)
for filename in files_to_convert:
    if filename.endswith(".py"):
        # Create the target file name with .exe extension
        target_file = os.path.splitext(filename)[0] + ".exe"
        source_file_path = os.path.join(source2_dir, filename)  # Use source2_dir
        source_file_path= source_file_path.replace('.exe','')
        
        target_file_path = os.path.join(target_dir, target_file)

        # Use pyinstaller to convert the Python file to an executable and specify the output directory
        # subprocess.call(["pyinstaller", source_file_path, "--distpath", target_dir, "--noconfirm",

        FileLocation = FileLocation +1
        
        subprocess.call(["pyinstaller", source_file_path, "--distpath", target_dir, "--noconfirm", "--onefile"
        # subprocess.call(["pyinstaller", source_file_path, "--distpath", target_dir, "--noconfirm"
                # "--hidden-import", "pyppdf",
                # "--hidden-import", "pyppdfium2",
                # "--hidden-import", "jinja2",
                # "--hidden-import", "pysqlite2",
                # "--hidden-import", "MySQLdb",
                # "--hidden-import", "psycopg2"
                ])
        
        print(str(FileLocation)+'/'+ str(numberOfFilesToConvert) )

       # # Clean up the temporary build directory created by pyinstaller
        # shutil.rmtree(os.path.join(target_dir, "build"))
        # shutil.rmtree(os.path.join(target_dir, "dist"))
        # os.remove(os.path.join(source_file_path + ".spec"))


# LocationUsedSource = 'importedDataPyimageFolderLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)


# LocationUsedSource = 'importedDataPyimageFolderLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyimageFolderLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyinternalLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyexcelLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyimageFolderLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyupdateNamesFile'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'importedDataPyFilesInDatabaseLocation'
# LocationUsedDestination = 'AddToDatabase'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)

# LocationUsedSource = 'GetDbDataFunction'
# LocationUsedDestination = 'GetDbData'
# MoveFiles(target_dir,LocationUsedSource, LocationUsedDestination)


print("Conversion to executable files is complete.")
