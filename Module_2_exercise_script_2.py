# Syniah Peterson
word = input('Enter a string: ')
lower = ""
upper = ""
for i in word:
    if ord(i) == 32:
        continue
    elif ord(i) >= 97 and ord(i) <= 122:
        lower += i
    else:
        upper += i
print(lower + upper)