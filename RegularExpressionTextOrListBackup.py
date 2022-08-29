
import re

#Replace all white-space characters with the digit "9":

txt = "The, rain,                in 7777777,Spain///[]<<<<<<<<<<>>>>>>>>>çççççççç============&&&&&&&&,|||||||"

# txt = '''['car',"dog","fish"]'''


# # # # x = re.sub("[^\s, ^S]", "9", txt)

# # # # x = re.sub("[^A-Z,^a-z,^[, ^], ^/]", "9", txt)

# # # # x = re.sub("[^A-Z,^a-z]", "9", txt)

# # # # x = re.sub("[^A-Z,^a-z,\d]", "9", txt)

# # # # x = re.sub("[^\w,^/]", "9", txt)

# # # # x = re.sub("[^[]", "9", txt)

# # # # x = re.sub("[^\w,^/,^[]", "9", txt)

# # # # x = re.sub("]", "9", txt)

# # # # x = re.sub("[^\w,^/,^[,^\\]]", "9", txt)     # this has support for latin caracters and other

# # # # x = re.sub("[^A-Z,^a-z,\d,^/,^[,^\\]]", "9", txt)       # this only has suport for american characters

# # # # x = re.sub("[^A-Z,^a-z,\d,^/,^[,^\\]]", "", txt)       # this only has suport for american characters

# # # # x = re.sub("[^A-Z,^a-z,\d,^/,]", "9", txt)       # this only has suport for american characters



if TextInput:
    if ForDatabase:
        x = re.sub("[^A-Z^a-z\d^/]", "", txt)     # For database Input
                                                  #  this only has suport for american characters   ## this is for text support (2)

    else:
        x = re.sub("[^A-Z^a-z\d]", "", txt)       # for UserText Input 
                                                  # this only has suport for american characters   ## this is for text support (2)
else:
    if txt[0] == '[':                             # this if for checking lists
        if txt[-1] == ']':
            # x = re.sub("[\"\']", "", txt) 
            x = txt                               # this does not change the list data if it´s a list
    else:
        x = ''

print(x)