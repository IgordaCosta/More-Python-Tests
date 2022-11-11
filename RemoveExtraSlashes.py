


def RemoveExtraSlashes(TextToRemoveSlashes):
    TextToRemoveSlashes1 = TextToRemoveSlashes.replace('/','\\')

    TextToRemoveChars2 = '\\'.join([i for i in TextToRemoveSlashes1.split('\\') if i !=''])

    return TextToRemoveChars2



# TextToRemoveSlashes = 'C/////Users\\\\\\\\Tigereye\\\\\\\\Desktop\\\\\\\\Apps\\\\\\\\CSSAutoFormFiller2\\\\\\\\CSSAutoFormFiller\\\\\\\\_clientImageFiles'

# print(RemoveExtraSlashes(TextToRemoveSlashes))