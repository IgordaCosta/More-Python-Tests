
import re


s="Hello$@, Python-------0123,456789$"

s1=re.sub("[^A-Za-z0-9,]","",s)
print(s1)