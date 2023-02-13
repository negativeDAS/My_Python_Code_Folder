fhandle = open('mbox-short.txt')
count = 0
dicna = dict()
for iter in fhandle :
    if not iter.startswith("From:"):
        continue
    lis = iter.split()
    word = lis[1]
    dicna[word] = dicna.get(word, 0) + 1
g_key = None
g_value = None
for key,value in dicna.items() :
    if g_value == None or value > g_value  :
        g_key = key
        g_value = value
print(g_key, g_value)
