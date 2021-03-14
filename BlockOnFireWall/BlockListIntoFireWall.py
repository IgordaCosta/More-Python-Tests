import win32com.shell.shell as shell

import pprint

import getListFromtxtfile





def BlockListIntoFireWall(filePathist,ruleNameList=[]):

    for i in range(len(filePathist)):

        if ruleNameList == []:
            fileCompName=filePathist[i].split('\\')[-1]
            FileOnlyName = fileCompName.split('.')[-2]

        else:
            FileOnlyName = ruleNameList[i]

        # commands = 'netsh advfirewall firewall add rule name="'+ FileOnlyName +'" dir=in action=block program= "'+ filePathist[i] +'" enable=yes profile=any'
        commands = 'netsh advfirewall firewall add rule name="'+ FileOnlyName +'" dir=out action=block program= "'+ filePathist[i] +'" enable=yes profile=any'
        
        pprint.pprint(commands)
        
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)




Location = r'C:\Users\IgorDC\Desktop\PydocTest' + '\\'

fileName = 'officeFileExeLocations.txt'




filePathist = getListFromtxtfile.getListFromtxtfile(Location,fileName)


BlockListIntoFireWall(filePathist)

print('DONE')