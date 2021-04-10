import ForceCpuUsage






TimesToDo = 2

######## TimesToDo
############ 1 for 40 secs
############ 2 for 1 min and 20 secs

multipleOfStrength = 2

######## multipleOfStrength
############ 1 for 30%CPU usage
############ 2 for 55% CPU usage
############ 3 for 90% and above CPU usage



ForceCpuUsage.CPUstresser(TimesToDo,multipleOfStrength)

print('Done')