# Syniah Peterson
num = 0
nums = []
evenNums = []
while num != 'QUIT':
    num = input('Enter a number or QUIT to quit: ')
    nums.append(num)
for i in range(len(nums)):
    if nums[i] == 'QUIT':
        nums.remove('QUIT')
    else:
        continue
for i in range(0, len(nums)):
    nums[i] = int(nums[i])
for i in range(0, len(nums)):
    if nums[i] % 2 == 0:
        evenNums.append(nums[i])
print('All Nums: ' + str(nums))
print('Even Nums: ' + str(evenNums))