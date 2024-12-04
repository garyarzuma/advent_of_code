import fileinput 

# Returns 1 if safe or 0 if not given a list of nums. Ex) [5, 3, 2, 6] -> 0 
def isSafe(nums):
    diffs = [];

    # Create diffs ex) [5, 3, 2, 6] -> [-2, -1, 4]:
    for x in range(len(nums)-1):
        val = int(nums[x+1]) - int(nums[x])
        diffs.append(val)
    
    # Check diffs for > 3, 0s and all match sign of diffs[0]
    for num in diffs:
        if(abs(num) > 3 or num == 0 or num*diffs[0] < 0):
            return 0;

    return 1

num_safe = 0;

for line in fileinput.input(files='input', encoding="utf-8"):
    nums = line.rstrip().rsplit(' ')
    diff_array = [];
    flag = 1;
    last = None; 
    num_safe += isSafe(nums) 

print(num_safe)
