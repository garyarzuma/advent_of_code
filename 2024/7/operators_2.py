import fileinput

input = fileinput.input('input')

mySum = 0


def next(prev, nums, i, ans, ops):

    if prev == ans:
        return True
    if i == len(nums):
        return False

    prev1 = prev * nums[i]
    prev2 = prev + nums[i]

    return (next(prev1, nums, i+1, ans, ops + '*') or
            next(prev2, nums, i+1, ans, ops + '+'))


for line in input:
    ans, nums = line.split(':')
    ans = int(ans)

    nums = nums.lstrip(' ').rstrip('\n').split(' ')
    nums = list(map(int, nums))

    if next(nums[0], nums, 1, ans, ''):
        mySum += ans

print(mySum)
