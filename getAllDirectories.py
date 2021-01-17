import os
import pprint

import getDirSize

saveLocation = r'C:\Users\IgorDC\Desktop\FileSizes\FileSizes.txt'

# directory= r'C:\Users\IgorDC\Desktop'

directory= r'C:\\'

# pprint.pprint([x[0] for x in os.walk(directory)])


# with open(saveLocation, 'w') as f:
#     f.write('Doe, a deer, a female deer\n')
#     f.write('Ray, a drop of golden sun\n')

with open(saveLocation, 'w') as f:
    DirectoryList = [x[0] for x in os.walk(directory)]
    for line in range(len(DirectoryList)):

        ShortSimple,ByteExpefic = getDirSize.getDirSize(DirectoryList[line])
        f.write(str(line+1) + ' .... ' + 'Directory Size in Bytes:,' + str(ByteExpefic) + ', or simply: ,' + str(ShortSimple)+ ",        ," + DirectoryList[line]+'\n')
      


print("Done!")