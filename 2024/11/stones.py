import fileinput

nums = []

for line in fileinput.input('input'):
    nums = line.rstrip('\n')
    nums = nums.split(' ')

print(nums)


def split(nums, left):
    new = []
    if left == 0:
        return nums
    for i, num in enumerate(nums):
        if num == '0':
            new.append('1')
        elif len(num) % 2 == 0:
            mid = len(num)//2
            right = num[mid:]
            right = right.lstrip('0')
            if right == '':
                right = '0'
            new.append(num[:mid])
            new.append(right)
        else:
            new.append(str(int(num)*2024))
    return split(new, left - 1)


split = split(nums, 25)
print(len(split))
