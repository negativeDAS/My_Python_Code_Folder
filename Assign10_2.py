fhand = open('mbox-short.txt')
dic = dict()
lis1 = list()
lis = list()
liz = list()
hrs = list()
h = list()
count = 0
for iter in fhand :
    iter = iter.strip()
    lis.append(iter)
for iter in lis :
    if not iter.startswith('From') :
        continue
    lis1.append(iter)
for word in lis1 :
    liz = word.split()
    try :
        hrs.append(liz[5])
    except :
        liz.clear()
        continue
    liz.clear()
for word in hrs :
    word = word.split(':')
    h.append(word[0])

for word in h :
    dic[word] = dic.get(word, 0) + 1

for key,val in sorted(dic.items()) :
    print(key,val)
