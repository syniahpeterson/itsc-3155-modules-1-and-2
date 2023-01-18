# Syniah Peterson - Problem: outputs duplicate and one appearance
from collections import Counter
firstList = []
secondList = []
for i in range(10):
    num = int(input('Enter number ' + str(i + 1) + ': '))
    firstList.append(num)
    # Problem with Counter
    once = Counter(firstList)
    if once[i] == 1:
        secondList.append(firstList[i])
print(once)
print('Original List: ' + str(firstList))
print('Nums that appear once: ' + str(secondList))