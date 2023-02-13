import re

lis1 = list()

fhand = open('Actual_Data.txt')
for iter in fhand :
    if re.search('[0-9]+', iter) :
        lis = re.findall('[0-9]+', iter)
        for num in lis :
            lis1.append(int(num))


print(sum(lis1))
