import re


def FindNumberWordInString(word, stringUsed):

    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), stringUsed))

    return count



# word= "dog"

# stringUsed ='dog cat dog puddle guinnipig dog'


# count = FindNumberWordInString(word, stringUsed)

# print(count)

