import time

millis = int(round(time.time() * 1000))

print(millis)



for i in range(50):
    print("EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")


millis2 = int(round(time.time() * 1000))

print(millis2)

print('it took ' ,millis2-millis, 'milliseconds to complete')

