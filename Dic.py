#A list is a linear collection of values that stay in order
#A dictionary is a bag of values, each with its own label
#A dictionary:
#is python's most powerful data collection
# allows us to do fast databases-like operations in python

# Dictionaries are like bags--no order
# So we index the things we put in the dictionary with a 'lookup tag'
bag = dict()
bag['books'] = 4
bag['notebook'] = 10
bag['pens'] = 21

print(bag)
print(bag['notebook'])

bag['notebook'] = bag['notebook'] + 50
print(bag)

#A program to print the how many times a word reappears in a string
str = input('Enter a sentence: ')
di = dict()
lis =  str.split()
for iter in lis :
    if iter not in di :
        di[iter] = 1
    else :
        di[iter] = di[iter] + 1
print(di,': Is the count of all words that are in the string')

# The same program done above can done more easily by a built-in python function for dictionaries i.e., dic.get(key , 0) where '0' is a defaultvalue that the function will return with the key if the key does not exists in the dictionary
lis1 =  str.split()
din = dict()
for count in lis1 :
    din[count] = din.get(count, 0) + 1

print(din,': Is the count of all words that are in the string using get func')

print('\n\n')
#if we simply for loop a dictionary the iteration variable will be the key

diction = {'anubhav' : 18, 'car' : 22, 'biscuit' : 15}

for key in diction :
    print(key, diction[key])

print(list(diction))
print('\n')
print(diction.keys())
print('\n')
print(diction.values())
print('\n')
print(diction.items())
print('\n')

#We loop through the key - value pairs in a dictionary using * two * iteration variables
#Each iteration , the first variable is the key and the second variable is the corresponding value for the key
for key,val in diction.items() :
    print(key, val)

print('\n\n')

fil = input('Enter the file name: ')
fhand = open(fil)
dicn = dict()
words = list()
for line in fhand :
    words = line.split()
    for word in words :
        dicn[word] = dicn.get(word, 0) + 1

print(dicn)
print('\n')
g_key = None
g_value = None
for key,value in dicn.items() :
    if g_value == None or value > g_value  :
        g_key = key
        g_value = value
print(g_key, g_value)
