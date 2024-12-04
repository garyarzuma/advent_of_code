import fileinput
import re 

input = fileinput.input(files='input', encoding="utf-8")
total = 0;
enabled = True;

for line in input:
    l, r = 0, 12;
    while l < len(line) - 11:
        stringMatch = re.search(r"\bmul\(\d{1,3},\d{1,3}\)", line[l:r])
        disableMatch = re.search(r"\bdon't\(\)", line[l:r])
        enableMatch = re.search(r"\bdo\(\)", line[l:r])

        if not enabled and enableMatch:
            enabled = True;
            l += 4
        elif enabled and disableMatch:
            enabled = False;
            l += 6
        elif enabled and stringMatch:
            numMatch = re.findall(r"\d{1,3}", stringMatch.group())
            num1 = int(numMatch[0]);
            num2 = int(numMatch[1]);
            total += num1*num2;
            l += stringMatch.span()[1];
        else:
            l += 1
        r = l + 12;

print(total);
