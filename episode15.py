'''
Here is the Python script that corresponds to the 15th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''



'''
Tuple
literal = (x,x,x,x,...,x,x)
Tuples are like lists. The difference between the two is that tuples are immutable 
while strings are immutable.
'''


'''
Mutable - can be changed in place. Supports item assignment.
Immutable - cannot be changed and doesn't support item assignment.
'''

mutable = [1,2,3,4,5,6,7,8,9,10]

mutable[0] = 'one' #change the first value of mutable to 'one'. 
#This works because lists are mutable.

print(mutable)


string_var = 'abcdefg' # strings are immutable.

#string_var[0] = 'A' # if we try to do the same with a tuple, 
# we get an error since tuples are immutable.


immutable = (1,2,3,4,5,6,7,8,9,10)

#immutable[0] = 'A' # if we try to do the same with a tuple, 
# we get an error since tuples are immutable.



'''
slicing
'''
print( immutable[:len(immutable)//2] ) # first half of the tuple.



'''
reversed
'''
print( immutable[::-1] )



'''
tuple concatenation:
'''
tuple1 = (1,2,3)
tuple2 = (4,5,6)
newtuple = tuple1 + tuple2

print(tuple1, tuple2, tuple3, sep='\n') # the original tuples are not altered.



'''
count
'''
count_this = ('one', 'two', 'three', 'one', 'two', 'three', 'one')
print( count_this.count('one') ) # returns the number of occurrences of 'one' (3).



'''
get the index of an element
'''
print( immutable.index(1) )



'''
To cast a tuple into a list, we can pass it to the list function.
to cast a tuple from list to string, we can pass it to the string function but 
this is a string representation of the tuple. Sometimes we want the elements of the 
tuple combined to form a string. To do that we use the join function like we did
in the previous episodes with lists.
'''




convert_me = ('This', 'is', 'a', 'tuple', 'to', 'convert', 'which', 'contains', \
'numbers', 'like', 1, 2, 3)

print( list(convert_me) ) # list representation

print( str(convert_me) ) # string representation

print( ' '.join(list( map(str, convert_me)) )) # first use map to convert the element to str



'''
Use tuples over lists when you don't want the data of a sequence to be modified. 
If you know the data of a sequence won't be modified, using a tuple over list 
is more efficient.
'''