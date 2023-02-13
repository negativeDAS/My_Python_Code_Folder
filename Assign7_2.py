import re
fname = input('Enter file name: ')
fhandle = open(fname)
count = 0
num = []
word = 0
res = 0
fs = 0
for iter in fhandle :
    iter = iter.rstrip()        #The new line is considered "whitespace"
    if not iter.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
fhandle1 = open(fname)
for iter in fhandle1 :
    if iter.startswith('X-DSPAM-Confidence:') :
        res = re.findall(r"[-+]?\d*\.\d+|\d+", iter)
        num.append(res[0])

for iter in num :
    fs = float(fs) + float(iter)

print('Average spam confidence:',fs / count)
