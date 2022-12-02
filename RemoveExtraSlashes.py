


def RemoveExtraSlashes(TextToRemoveSlashes):

    TypeTuppleUsed = False
    if type(TextToRemoveSlashes) == type(()):
        TextToRemoveSlashes00 = TextToRemoveSlashes
        TextToRemoveSlashes = list(TextToRemoveSlashes00)
        TypeTuppleUsed = True

    TextToRemoveSlashes1 = TextToRemoveSlashes.replace('/','\\')
    TextToRemoveChars2 = '\\'.join([i for i in TextToRemoveSlashes1.split('\\') if i !=''])

    if TypeTuppleUsed:
        TextToRemoveChars200 = TextToRemoveChars2
        TextToRemoveChars2 = tuple(TextToRemoveChars200)

    return TextToRemoveChars2


# print(type(()))

# TextToRemoveSlashes = 'C/////Users\\\\\\\\Tigereye\\\\\\\\Desktop\\\\\\\\Apps\\\\\\\\CSSAutoFormFiller2\\\\\\\\CSSAutoFormFiller\\\\\\\\_clientImageFiles'

# print(RemoveExtraSlashes(TextToRemoveSlashes))