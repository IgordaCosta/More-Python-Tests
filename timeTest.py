import time    
timegotten1 = time.time()

# timegotten11 = int(time.time()*1000)

timegotten11 = int(timegotten1*1000)


print(timegotten1)
print(timegotten11)

timegotten2 = time.time()

print(timegotten2)

# timegotten22 = int(time.time()*1000)

timegotten22 = int(timegotten2*1000)


print(timegotten2)

print(timegotten22)

changeIntime = timegotten2-timegotten1

changeIntime2 = timegotten22-timegotten11


print(changeIntime)

print(changeIntime2)






# import datetime, time
 
# # secs = 123456789.1236

# secs = changeIntime *100000000

# print(secs)
 
# TimetoFinish = datetime.timedelta(seconds = secs)

# print(TimetoFinish)
 






