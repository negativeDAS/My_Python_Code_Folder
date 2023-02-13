#hello hello dude
#A List is a collection that allows us to put many values in a single variable
#for example:
hola = ['hello', 'Hii', 'Say', 'goodbye']
print(hola)
# A list can be a collection of any python object even an another List
# A list can be empty
pr = [['membrane keyboard', 'mechanical keyboard'], 'mouse', 'monitor']
print(pr)
#lists and definite loops are best pals
for greet in hola :
    print(greet,'guise')
print('See ya all')
#Just like strings, we can get any single element in a list using an index specified in a square brackets
print(hola[1])      #The indexing of list is done from 0
#Strings are "immutable"- We cannot change the contents of a string- we must make a new string
#But lists are "mutable"-we can change an elementof a list using the index operator
hola[1] = 'Aloha'
print(hola)
# to get the length of a alist we can use len() function
print(len(hola))        #len() takes list as a parameter and return the number of elements in a list

#range() fumction
#range() function returns a list of numbers that range from zero to one less than the parameter
#We can construct an index loop using for and an integer iterator
for iter in range(len(hola)) :
    print(iter, end=' ')                #end=' ' is used to print somthing in the same line
print('\n')
#print the elements of a list by two methods:
#1st we have done already in line 11
#2nd by using range() function
for i in range(len(hola)) :
    j = hola[i]
    print(j,'bro')

#Concatenating lists
greet = ['Thank you','fine','see ya']
print(hola + greet)
print(len(hola + greet))

#lists slicing: works exactly as strings "upto but not including" :
print(hola[1:3])
print(hola[:2])
print(hola[1:])
print(hola[:])

#list methods
x = greet
print(type(x))
print(x)


#we can create a list by adding in the elements in it using append function
bag = list()
bag.append('Books')
bag.append('Pen')                       #the list stays in order by using the append() function the new elements are added at the end
bag.append('Notebook')
bag.append('ipad')
print(bag)

#A list can be sorted using list.sort() same as string function
#if there are strings in the list then Then the one that starts with the capital letters are sorted in the starting of the string then after comes the small letter ones
hola.sort()
print(hola)

#built-in functions in lists

lsi = [3, 41, 12, 9, 74, 15]

#1st len()
print(len(lsi))

#2nd max()
print(max(lsi))

#3rd min()
print(min(lsi))

#4th sum()
print(sum(lsi))
print('\n\n')
#program to find average of the numbers without using sum function

summ = 0
count = 0
while True :
    num = input('Enter a number: ')
    if num == 'done' or num == 'Done' :
        break
    summ = summ + int(num)
    count = count + 1

avg = summ / count
print('Average =',float(avg))

#program to find average of the numbers using lists and the sum functions
liss = list()
while True :
    num1 = input('Enter a number: ')
    if num1 == 'done' or num1 == 'Done' :
        break
    value = float(num1)
    liss.append(value)

avrge = sum(liss) / len(liss)
print('Averge this time:',float(avrge))

print('\n\n')

#split() split a string separated by any character called delimiter, by default its space, multiple spaces are treated like one delimiter
str = 'I : am : back : here : haaah'
plp = str.split()
print('Variable plp',plp)
print('variable str":',str)
plp1 = str.split(':')
print('variable plp1',plp1)
