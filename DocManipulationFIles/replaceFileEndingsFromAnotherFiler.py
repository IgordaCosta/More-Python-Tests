

fileLocation =r'C:\Users\Tigereye\Documents\AutoFormFillerFiles\file1.jpg'

newFileLocation0 = r'C:\Users\Tigereye\Documents\AutoFormFillerOutputFiles\file2replace.jpg'

fileLocation1 = '\\'.join(fileLocation.replace('\\', '/').split('/')[:-1])



fileLocation2 = fileLocation1 + '\\' + newFileLocation0.replace('\\', '/').split('/')[-1]

print(fileLocation2)