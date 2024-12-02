import fileinput 

num_safe = 0;

for line in fileinput.input(files='input', encoding="utf-8"):
    nums = line.rstrip().rsplit(' ')
    diff_array = [];
    flag = 1;
    last = None; 
    for x in range(len(nums)-1):
        val = int(nums[x+1]) - int(nums[x])
         
        if(abs(val) > 3 or val == 0):
            flag = -1;
            break;
        
        if(last != None and (last*val) <= 0):
            flag = -1    
            break;
        
        last = val;

    if flag > 0:
        num_safe += 1;

print(num_safe)
