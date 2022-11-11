# import random
import os
import numpy

from SnL import *

# list1 = ['a', 'b', 'c', 'd']

# numpy.random.seed(434447953)
# numpy.random.shuffle(list1)

# print(list1)



  
def DefConst():
    

    # print(os.getpid())

    # print(str(os.getpid()).zfill(3))


    IDS =os.getpid()



    # print(time.time())


    # LL = str(time.time())[-2:]

    # Rv = str(time.time())[-4:-3]

    #Int Data Senha

    # IDS = time.time()

    #Data Senha
    DSn = str(IDS)    

    #ListL ocation
    LL = int(DSn[-2:])

    #Random Value
    # Rv = int(DSn[-3:-2])     

    # print(LL)

    # print(Rv)

    #Location Choosen
    LC = SnL[LL]            

    #Small List Choosen
    SLC = list(LC[34:57])

    # print(SLC)


    # print(int(str(int(IDS*100000))[-3])/10)

    
    # glRandLen = int(len(str(IDS)))
    # if glRandLen>3:
    #     glRand = int(int(int(str(IDS)[-3])+int(str(IDS)[-2]))/2)/20
    #     # print(glRand)
    # else:
    #     glRand = 0.7


    numpy.random.seed(IDS)
    numpy.random.shuffle(SLC)

    # Aleatorio Small String Choosen
    ASSC = ''.join(SLC)

    # print(ASSC)




    #Small List Choosen 2
    SLC2 = list(LC[72:83])

    numpy.random.seed(IDS)
    numpy.random.shuffle(SLC2)
    # Aleatorio Small String Choosen
    ASSC2 = ''.join(SLC2) + '.db'

    # print(ASSC2)

    return ASSC2, ASSC



print( DefConst())

