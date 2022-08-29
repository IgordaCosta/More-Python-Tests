import AddToble
import GetWriteDBTableSecured


def insertIntoDatabase(NameItem, ValueItem):

    GetWriteDBTableSecured.DeleteDb()

    AddToble.AddToable(NameItem=NameItem,ValueItem=ValueItem)
