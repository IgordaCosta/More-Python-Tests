


def ExcelNumberToColumnLetter(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string




# letter=ExcelNumberToColumnLetter(753)

# print(letter)