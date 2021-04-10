import os
import time
import psutil
from subprocess import Popen, PIPE




def ParallelProccessing0(multiple):

    # CommandFile = 'forLoop.py'

    CommandFile = r'C:\Users\IgorDC\Desktop\Apps\ForceCpuUsage\forLoop.py'

    FunctionName = ' forLoop'

    commandUsed = 'python ' + CommandFile + FunctionName

    AddValuee= ' | ' +  commandUsed

    AllAddValues = (' | ' +  commandUsed) * multiple

    AllCommandUsed = commandUsed + AllAddValues

    # stream = os.popen(AllCommandUsed)

    os.popen(AllCommandUsed)
    # output = stream.read()

    # return output




def ParallelProccessing(multiple):


    CommandFile = r'C:\Users\IgorDC\Desktop\Apps\ForceCpuUsage\forLoop.py'

    FunctionName = ' forLoop'

    commandUsed = 'python ' + CommandFile + FunctionName
   
    if multiple < 1:
        multiple = 1

    cmds_list = [commandUsed] * multiple

    procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]

    for proc in procs_list:
        proc.wait()




def CPUstresser(TimesToDo,multipleOfStrength):

    multiple = multipleOfStrength

    for time in range(TimesToDo):
        # DoneOutput = ParallelProccessing(multiple)
        ParallelProccessing(multiple)

    
    # return 'Done ' + str(TimesToDo) + ' times'




def StartCpuStressIfLessLimit(MustHaveStressLimit, TimesToDo, multipleOfStrength):
    while True:

        time.sleep(10)

        CpuCurrentUsage = psutil.cpu_percent()

        print(CpuCurrentUsage)

        if  MustHaveStressLimit > int(CpuCurrentUsage):
            print('usage Less then 20')
            print('stating stress Function')

            #### CPUstresser function goes here        
            CPUstresser(TimesToDo,multipleOfStrength)