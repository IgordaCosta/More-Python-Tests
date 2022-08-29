import GetWriteDBTableSecured

# NameItem = ['a','b', 'c']


# ValueItem =1


# NameItem = 'q'

def AddToable(NameItem, ValueItem):

    if type(NameItem) == type([]):
        print('is list')

        ItemNameList = NameItem

        colValueList = ValueItem

        GetWriteDBTableSecured.WriteTableSecuredList(ItemNameList=ItemNameList, colValueList=colValueList)


    else:
        print('not list')

        ItemName = NameItem

        ItenValue = ValueItem

        GetWriteDBTableSecured.WriteTableSecuredIten(ItemName=ItemName,ItenValue=ItenValue)

