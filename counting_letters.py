word = input('Enter a word: ')
count = 0
s_letter = input('Enter the letter you want to search: ')
for letter in word :
    if letter is s_letter :
        count = count + 1
print('The number of',s_letter,'in',word,'is',count)

str1 = 'Hello'
str2 = 'There'
print(str1 + str2)
x = '40'
y = int(x) + 2
print(y)
