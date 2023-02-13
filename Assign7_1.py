fname = input('Enter file name: ')
fhand = open(fname)

for iter in fhand :
    iter = iter.upper()
    iter = iter.rstrip()
    print(iter)
