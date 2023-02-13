#                   .....REGULAR EXPRESSION.....
#   In computing, a regular expression, also referred to as 'regexp', provides a
#   concise and flexible means for matching strings of text, such as particular
#   characters, words, or patterns of characters. A regular expression is written
#   in a formal language that can be interupted by a regular expression processor

#                   .....characterstics of Regular Expression......
#   -> Very powerful and quite cryptic.
#   -> Regular expressions are a language unto themselves.
#   -> A language of "marker characters"- programming with characters.
#   -> It is a kind of "old school"  language -compact

#           .....Regular Expression quick guide.....
#   ^           Matches the beginning of a line
#   $           Matches the end of the line
#   .           Matches any character
#   \s          Matches whitespace
#   \S          Matches any non-whitespace character
#   *           Repeats a character zero or more times
#   *?          Repeats a character zero or more times (non-greedy)
#   +           Repeats a character one or more times
#   +?          Repeats a character one or more times (non-greedy)
#   [aeiou]     Matches a single character in the listed set
#   [^XYZ]      Matches a single character not in the listed set
#   [a-z0-9]    The set of characters can include a range
#   (           Indicates where string extraction is to start
#   )           Indicates where string extraction is to end


import re

fhand = open('mbox-short.txt')

count = 0

for iter in fhand :
    iter = iter.rstrip()
    if re.search('^From:', iter) :                 #Basic program to find Lines in the files starting with 'From:'
        print(iter)                                #withot using string funtions(str.startswith())

#                  ......Wild -Card Characters(Checking for the data)......
#The dot character matches any charecter
#If i add the asterisk character, the character is 'any number of times'
#For example: "^X.*:" <-- This regular expression will read as 'Search for lines that start with(^) X Followed by any nubers of character followed by a colon(:)'
#"^X-\S+:" <-- This RE will read as "Search for lines that start with 'X-' Followed by any non-whitespace character Followed by one or more non-blank character followed by a colon(:)"
#                   ......Matching and Extracting Data.........
#   re.search() returns a True/False depending on whether the sting matches the regular expression
#   If we actually want the matching stings to be extracted, we use re.findall()
fhand1 = open('mbox-short.txt')

for iter in fhand1 :
    iter = iter.rstrip()
    if re.search('^X.*:', iter) :
        print(iter)
        count = count + 1


count2 = 0

fhand2 = open('mbox-short.txt')

for iter in fhand2 :
    iter = iter.rstrip()
    if re.search('^X-\S+:', iter) :
        print(iter)
        count2 = count2 + 1

print(count)
print(count2)

#              ...........Extrating the Data using regular expressions...........
#   The above used re.search() function only returns true or false so by the help of that we can only check for a particular data
#   in order to retrieve that data we use re.findall() function, it basically returns a list of strings of things that are true as per the reg. exp.

x = 'here all 4 of us are eating 25 burgers all at 1'
y = re.findall('[0-9]+', x)         #it basically means to find one or more number in the string, we donot use * because its silly none or more number makes no sense
print(y)

y1 = re.findall('[AEIOU]+', x)
print(y1)

#               ........Greedy Matching .........
#   The repeat characters(* and +) Push outwards in both the directions (greedy) to match the largest possible string.
#   For Example:

x2 = 'Find: Using the : characters'

y3 = re.findall('^F.+:', x2)            #Greedy Matching
print(y3)

#           ......Non-Greedy Matching.......
#   If we add ? after repeat characters (* and +) then it will chill out a bit

y4 = re.findall('^F.+?:', x2)            #Non-Greedy Matching
print(y4)

x3 = 'From stephen.marquarzd@uct.ac.za Sat Jan 5 09:14:16 2008'

y5 = re.findall('\S+@\S+', x3)
print(y5)

fhand3 = open('mbox-short.txt')

for iter in fhand3 :
    iter = iter.rstrip()
    print(re.findall('^From (\S+@\S+)',iter))
