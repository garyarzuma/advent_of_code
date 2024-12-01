import fileinput 

list1 = [];
list2 = [];

for line in fileinput.input(files='input', encoding="utf-8"):
    list = line.rstrip().partition('   ')
    list1.append(list[0])
    list2.append(list[2])

list1.sort()
list2.sort()

listSums = [];

for x in range(len(list1)):
    listSums.append(abs(int(list1[x]) - int(list2[x])))

distance = 0;

for num in listSums:
    distance += num;

print(distance)


