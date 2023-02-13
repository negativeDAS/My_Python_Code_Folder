strng = input('Enter a Word or a sentence or a phrase: ')
index = 0
count = 0
wo = strng[2]
print('The Third letter of the given string is:',wo)             #Third, not second because indexing in string is done from 0
#Application of all the functions of string
#1st is len(str) where str is a variable in which a string is stored it can have any name
print('We are looping through the string right here')
lngth = len(strng)
print('The length of the given string is:',lngth)

while index < lngth :
    print(strng[index])                                           #looping through strings using while looping
    index = index + 1

for letter in strng :                                             #doing the same thing using foer loop. For loop is more elegant and viable than while
    print(letter)

#program to count he number of a particular letter or a substring in a string which will be the value stored in wo i.e., The third letter of any string
print('We are counting the number of',wo,'here')
for letter in strng :
    if letter == wo :
        count = count + 1

print('The number is:',count)

#slicing of strings
print('We are doing some slicing here: ')
print(strng[0 : 4])                         #in [from where the slicing starts : till where the sliing is to be done but not including the number]
print(strng[3 : 4])
print(strng[7 : 100])                       #if second number is beyond the end of the string, it stops at the end
print(strng[ : 4])
print(strng[3 : ])                          #if we leave of the first or last or both of the number of slice, it is assumed to be thge beginning
print(strng[ : ])                           # and end of the string respectively.
#2nd is str.upper() and str.lower() where str is a variable in which a string is stored it can have any name
print('Playing with the upercase and lowercase string functions')
upstr = strng.upper()
print('Printing upstr:',upstr)
print('Printing the actual variable: ',strng,'shows no change in the actual variable')
lwrstr = strng.lower()
print('Printing lwrstr:',lwrstr)
print('Printing the actual variable: ',strng,'shows no change in the actual variable')
#3rd is str.capitalize()  where str is a variable in which a string is stored it can have any name
print('We are capitalizing the given string')
print(strng.capitalize())       #turns only the first letter of the string capital
#4th is str.find() function
pos1 = strng.find('welcome')
print('the welcome starts from the index:',pos1)
pos2 = strng.find('some')                    # if the letter or substring does not exists then it returns -1
print('The some starts from the index:',pos2)
#5th is str.replace('letter or substring of the known string' , 'New letter or substring')
#The str.replace() function is like "search and replace function" in a word proessor
#It replaces "all occurences of search string" with "replacement string"
rep = strng.replace('world' , 'Universe')
print(rep,'<- Printed the variable which holds the modified string')
print(strng,'<- Printed the actual string shows that change is occured in a copy of the string not the actual string')

#6th is str.lstrip(), str.rstrip() and str.strip()
# str.lstrip() and str.rstrip() remove whitespaces from left and right of the string
#str.strip() removes whitespaces from both left and right sides of the string
print(strng.lstrip())
print(strng.rstrip())
print(strng.strip())

#7th is str.startswith() It return either true or false depending on whether the string starts with a particular word or substring
print(strng.startswith('Hello'))
print(strng.startswith('hello'))
#8th parsing and extracting of a letter or a substring
#where a string of commands – usually a program – is separated into more easily processed components, which are analyzed for correct syntax and then attached to tags that define each component.
#The computer can then process each program chunk and transform it into machine language.
#for example: A program to find the extension of a gmail account of an email not encluding the @ sign
ext_s = strng.find('@')
ext_e = strng.find(' ' ,ext_s)          #Find can be entered with two parameters  1st the character to search and 2nd is the index from where to start the search
ext = strng[ext_s + 1 : ext_e]
print('The extension of the email address is:',ext)
#9th new line character \n
#newline(\n) is a single character not two
wor = 'how are you doin dude\nHope you are fine'
print(wor)
print(len(wor))

#10th str.split() function splits the string to form a word.
lis = strng.split()
print(lis)
