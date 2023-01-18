# Syniah Peterson
n = int(input('Enter a number: '))
nums = []
avg = 0
total = 0
for i in range(n):
    num = float(input('Enter number ' + str(i + 1) + ': '))
    nums.append(num)
    total += nums[i]
avg = total / n
print('List: ' + str(nums))
print('Average: ' + str(avg))