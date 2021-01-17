import os
from hurry.filesize import size

def getDirSize(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path+'\\'):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                try:
                    total_size += os.path.getsize(fp)
                except:
                    pass
        

    return size(total_size), total_size


# #C:\

# # start_path= r'C:\Users\IgorDC\Desktop'

# start_path1 = r'C:\Old PC'

# start_path2 = r'D:\Old PC'

# # start_path2 = r'C:\Users\IgorDC\Desktop\testSpeed'


# pathsize1 = getDirSize(start_path1)
# print('get_size(start_path1) bellow')
# print(pathsize1)


# pathsize2 = getDirSize(start_path2)
# print('get_size(start_path2) bellow')
# print(pathsize2)


# print('do they equal: ',str(pathsize1==pathsize2))