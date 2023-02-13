fhandle = open('mbox-short.txt')
count = 0
for iter in fhandle :
    if not iter.startswith("From:"):
        continue
    lis = iter.split()
    print(lis[1])
    count = count +1
print("There were", count, "lines in the file with From as the first word")
