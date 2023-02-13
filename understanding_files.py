count = 0
#using open()
# handle  = open(filename, mode)
#returns a handle use to manipulate the file
#filename is a string
#mode is optional and shhopulsd be 'r' if we are palnning to rwead the file
#and 'w' if we are going to write to the file
fhand = open('mock.txt')
print(fhand,'\n\n')
#File handle as a sequence
#a file handle open for 'read' can be treated as a sequence of strings where each line in the file is a strings
#We can use the 'for' statement to iterate through a sequence
#A sequence is an ordered set
for iter in fhand :                       #considers one line as single string(one line = string from starting to \n)
    iter = iter.rstrip()                  #The string already contains a new line and print statement adds up one
    print(iter)                          #more by its own so we will right strip that new line in the string

print('\n\n')
#Program to Count number of lines in a files

fil = open('mock.txt')

for line in fil :                      #considers one line as single string(one line = string from starting to \n)
    count = count + 1

print('no. of lines are: ', count)
print('\n\n')
#Reading the whole file (newlines and all) into aa single string
#fhandle.read()
CheckHand = open('mock.txt')
fileis = CheckHand.read()
print(len(fileis),'\n\n')         #using string len(str) function to get the number of characters in the files
                        #which has been stored a single string in the fileis variable by fhandle.read() function
print(fileis[:50],'\n\n')

#Sreaching through a file
#using str.startswith('substring') function to search a particular part
fhand2 = open('mock.txt')
for iter in fhand2 :
    iter = iter.rstrip()        #The new line is considered "whitespace"
    if iter.startswith('From') :
        print(iter)
print('\n\n')
#The same above program but intead of Printing a string we are going to skip that
fhand3 = open('mock.txt')
for iter in fhand3 :
    iter = iter.rstrip()        #The new line is considered "whitespace"
    if iter.startswith('From') :
        continue                        #skip

    print(iter)
print('\n\n')
 #Selecting a line with the help of in
fhand4 = open('mock.txt')
for iter in fhand4 :
    iter = iter.rstrip()        #The new line is considered "whitespace"
    if not 'uct.ac.za' in iter :
        continue                        #skip

    print(iter)
print('\n\n')
