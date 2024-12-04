import fileinput 

# Returns -1 if safe or ith position of problem diff if not given a list of nums. Ex) [5, 3, 2, 6] -> 2 
def unsafeLevelIndex(nums):
    diffs = [];

    # Create diffs ex) [5, 3, 2, 6] -> [-2, -1, 4]:
    for x in range(len(nums)-1):
        val = int(nums[x+1]) - int(nums[x])
        diffs.append(val)
    
    # Check diffs for > 3, 0s and all match sign of diffs[0]
    for i, num in enumerate(diffs):
        if(abs(num) > 3 or num == 0 or num*diffs[0] < 0):
            return i;

    return -1;

# Returns 1 if tolerably  safe, 0 if not 
def isTolerablySafe(nums, line):
    badIndex = unsafeLevelIndex(nums);
    
    if badIndex == -1 or badIndex == len(nums)-1:
        return 1;
     
    testListNoBadIndex = nums[:badIndex] + nums[badIndex+1:] 
    testListAfterBadIndex = nums[:badIndex+1] + nums[badIndex+2:]
    testListWithNewSign = nums[1:]
   
    firstCheck = unsafeLevelIndex(testListNoBadIndex)
    secondCheck = unsafeLevelIndex(testListAfterBadIndex)
    thirdCheck = unsafeLevelIndex(testListWithNewSign)

    if firstCheck == -1 or secondCheck == -1 or thirdCheck == -1:
        return 1;

    return 0;


num_safe = 0;

for i,line in enumerate(fileinput.input(files='input', encoding="utf-8")):
    nums = line.rstrip().rsplit(' ')
    diff_array = [];
    flag = 1;
    last = None; 
    num_safe += isTolerablySafe(nums, i) 

print(num_safe)
