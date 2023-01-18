# Syniah Peterson
words = []
for i in range(5):
    word = input('Enter a word: ')
    words.append(word)
for i in range(len(words)):
    wordString = ' '.join(words)
print('Words: ' + str(words))
print('One String: ' + str(wordString))