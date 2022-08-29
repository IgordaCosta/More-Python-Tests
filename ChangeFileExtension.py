import os


def ChangeFileExtension(fileName, NewFileExtension):

    # print(fileName)

    pre, ext = os.path.splitext(fileName)
    # print (pre)
    try:
        os.rename(fileName, pre + NewFileExtension)
        # print('Done')
    except:
        pass


# oldfExt= '.txt'

# NewFileExtension = '.txli '

# fileName = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles\test2' + '\\' + 'img1-2022-05-04_00-05-48_Txt' + oldfExt



# ChangeFileExtension(fileName, NewFileExtension)