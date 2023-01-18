# Syniah Peterson
nums1 = []
nums2 = []
common = []
i = 0
for i in range(5):
    num = int(input('Enter a number for the first list: '))
    nums1.append(num)

for j in range(5):
    num = int(input('Enter a number for the second list: '))
    nums2.append(num)

for k in range(5):
    if nums1[k] in nums2:
        common.append(nums1[k])
    else:
        continue
print('First List: ' + str(nums1))
print('Second List: ' + str(nums2))
print('Common List: ' + str(common))

