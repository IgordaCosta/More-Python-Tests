import win32com.shell.shell as shell



rule_name ='excel'

file_path = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'

commands = 'netsh advfirewall firewall add rule name="'+rule_name+'" dir=in action=block program= "'+ file_path +'" enable=yes profile=any'


##### this runs the commands in adminstrator mode
shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)




print('done')