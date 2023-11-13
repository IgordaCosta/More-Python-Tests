import os
import pprint

def list_files_and_directories(root_dir):
    resultFile = []
    resultDir = []

    for item in os.listdir(root_dir):
        path = os.path.join(root_dir, item)
        if os.path.isfile(path):
            if item.split('.')[-1]=='html':
                resultFile.append(item)
        elif os.path.isdir(path):
            resultDir.append(item + '/')

    return resultFile, resultDir

# Example usage:
directory_path = r'F:\Apps3\CSSAutoFormFiller7_Updated92Before4592\CSSAutoFormFiller'
resultFile, resultDir = list_files_and_directories(directory_path)

# Print the result as a single list
pprint.pprint(resultFile)

pprint.pprint(resultDir)
