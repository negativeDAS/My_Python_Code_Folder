fhandle = open('romeo.txt')
lis = []
for iter in fhandle :
    iter = iter.split()
    for i in iter :
        lis.append(i)
print(lis)
S = set(lis)
lis1 = list(S)
lis1.sort()
print(lis1)
