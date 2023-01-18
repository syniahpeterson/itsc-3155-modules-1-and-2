# Syniah Peterson
userString = input('Enter a string: ')
array = list(userString)
list = [array[i: i + 3] for i in range(0, len(array), 3)]
print(list)