



def DecimalToBinaryList(MaxListValue, ZeroPadding=False):

    Maxvalue = bin(MaxListValue)[2:]

    maxSize=len(Maxvalue)

    DicimalList = []

    BinaryList = []

    for number in range(MaxListValue+1):

        value = bin(number)[2:]

        if ZeroPadding:

            NumberOfZerosAppend='0'*(maxSize-len(str(value)))

            FixedSizeValue = NumberOfZerosAppend + str(value)

        else:

            FixedSizeValue = str(value)


        DicimalList.append(number)
        
        BinaryList.append(FixedSizeValue)

    return BinaryList, DicimalList






# MaxListValue= 1000

# BinaryList, DicimalList = DecimalToBinaryList(MaxListValue)


# print('BinaryList: ',BinaryList)

# print('DicimalList: ',DicimalList)