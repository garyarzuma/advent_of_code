import fileinput

nums = []

for line in fileinput.input('input'):
    nums = line.rstrip('\n')
    nums = nums.split(' ')

# print(nums)


def splitOnceNoMemo(num):
    new = []
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
    return new


def blink(processList):
    res = {}
    for numToProcess, count in processList.items():
        kids = splitOnceNoMemo(numToProcess)
        for kid in kids:
            if res.get(kid):
                res[kid] += count
            else:
                res[kid] = count
    return res


def blinkCountTimes(processList, count):
    for x in range(count):
        processList = blink(processList)
    total = 0
    for left, count in processList.items():
        total += count
    return total


processList = {}
for num in nums:
    processList[num] = 1

print(blinkCountTimes(processList, 75))
