# Syniah Peterson
array = [0, 0, 0, 0, 0]
row = int(input('Enter a row num from 1 to 5: '))
column = int(input('Enter a column num from 1 to 5: '))
while not row in range(0, 6):
    row = int(input('Enter a row num from 1 to 5: '))
while not column in range(0, 6):
    column = int(input('Enter a column num from 1 to 5: '))
for i in range(5):
    print(array)