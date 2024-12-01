import fileinput 

list1 = [];
list2 = {};

for line in fileinput.input(files='input', encoding="utf-8"):
    myList = line.rstrip().partition('   ')
    list1.append(myList[0])

    if(list2.get(myList[2])):
        list2[myList[2]] += 1;
    else:
        list2[myList[2]] = 1;

similarityScore = 0;

for num in list1:
    if(list2.get(num)):
        similarityScore += int(num) * list2.get(num);

print(similarityScore)


