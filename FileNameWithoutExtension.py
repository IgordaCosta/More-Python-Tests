



def FileNameWithoutExtension(filename):

    IdentifierName = '.'.join(filename.split('.')[:-1])

    return IdentifierName




# filename = 'abc2345.dgdfjdlkajdhfaljksdf.adsfsadf.asdf.txt'


# print(FileNameWithoutExtension(filename))