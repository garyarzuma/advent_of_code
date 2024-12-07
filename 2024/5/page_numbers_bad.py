import fileinput

input = fileinput.input(files='input', encoding="utf-8")

rules = {}
middle_page_sums = 0

for line in input:
    befores = []
    no_good = False

    if line.find('|') > 0:
        split = line.split('|')
        l, r = split[0], split[1].rsplit('\n')[0]

        if l in rules:
            rules[l].append(r)
        else:
            rules[l] = [r]
    elif line.find(',') > 0:
        split = line.rstrip('\n').split(',')
        for num in split:
            afters = rules[num]
            swapSpots = []
            for a in afters:
                if a in befores:
                    no_good = True
                    swapSpots.append(split.index(a))
            if no_good and len(swapSpots) > 0:
                swapSpots.sort()
                split.remove(num)
                split.insert(swapSpots[0], num)
            befores.append(num)
        if no_good:
            middle_page_sums += int(split[len(split)//2])

print(middle_page_sums)
