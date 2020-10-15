import os

def ForceCloseExcel():

    try:
        os.system('TASKKILL /F /IM excel.exe')

    except Exception:
        print("Excel not found")

# ForceCloseExcel()