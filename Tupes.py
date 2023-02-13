#Tuples are another kind of sequence that functions much like a list- they have elements which are indexed starting at 0
x = ('Anubhav', 'Laptop', 'Keyboard', 'Mouse')
print(x)
print(x[2])
y = (3, 5, 7, 34, 64)
print(y)
print('\n\n')
for iter in x :
    print(iter)

#                                               _____Lists are mutable_____
#______________ Unlike a list , once you create a tuple , you cannot alter its contents - similar to a string___________________


#>>> y = ' ABC '
#>>> y [ 2 ] = ' D '
#Traceback : ' str ' object does not support item Assignment
#>>> z = ( 5 , 4 , 3 )
#>>> z [ 2 ] = 0
#Traceback : ' tuple ' object does not support item Assignment
#________________Things not to do With Tuples______________
#>>> x = ( 3 , 2 , 1 )
#>>> x . sort ( )
#Traceback :
#AttributeError : ' tuple ' object has no attribute ' sort '
#>>> x . append ( 5 )
#Traceback :
#AttributeError : ' tuple ' object has no attribute ' append '
#>>> x.reverse ( )
#Traceback :
#AttributeError : ' tuple ' object has no attribute ' reverse '

(x, y) = ('Jokes', 33)
(a, s) = ('Hello', 39)
print(x, y, a, s)

#The items() function in dictionary returns a list of (key, value) tuples

diction = {'anubhav' : 18, 'car' : 22, 'biscuit' : 15}
liz = diction.items()
print(liz)

#The comparison operators work with tuples and other sequences . If the first item is equal , Python goes on to the next
#element , and so on , until it finds elements that differ .

(p, q, r, s) = (1, 5, 2, 7)
(l, m, n) = (1, 5, 4)
print((p, q, r, s) < (l, m, n))
print((x, y) < (a, s))


#We can do this even more directly using the built - in function sorted that takes a sequence as a parameter and returns a sorted sequence
