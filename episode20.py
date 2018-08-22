'''
Here is the Python script that corresponds to the 20th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Comparison can also be used on strings.

A - string A
B - string B

operators: ==, !=, >, <, >=, <=

A <operator> B -- compare A and B based on their character ordinal values.
'''

print( 'apple' < 'banana' ) # True

print( 'Apple' < 'apple' ) # True. ord('A') = 65; ord('a') = 97

print( 'apple' < 'Zebra' ) # False. Use lower or upper methods...

print( 'apple'.lower() < 'Zebra'.lower() )



'''
The same applies to other sequences
'''

list1 = [1,2,3,4]

list2 = [1,2,3,5]

print( list1 < list2 )



'''
Sets can also be compared.

A - set A
B - set B

A <= B  -   A is a subset of B
A < B   -   A is a proper subset of B
A == B  -   A is set equivalent to B
A >= B  -   A is a superset of B
A > B   -   A is a proper superset of B
'''

A = {1,2,3}
B = {1,2,3}

print( A <= B ) # True because all elements in A are in B.

print( A == B ) # True for the same reason.

print( A >= B ) # True because all elements in B are in A.

A.add(4)

print( A > B ) # True because now A is a proper superset.

B.add(4)

B.add(5)

print( A < B ) # True because now A is a proper subset. 



'''
Booleans are actually a third numeric type
True == 1
False == 0
'''

print(True == 1)

print(False == 0)


'''
Many types that we learned about can be implicitly evaluated as a boolean
Empty collections are generally False.
NonEmpty collections are generally True.
'''
# All of these are False

print( bool( '' ) )

print( bool( [] ) )

print( bool( () ) )

print( bool( set() ) )

print( bool( {} ) )

# All of these are True

print( bool( '1' ) )

print( bool( [1] ) )

print( bool( (1) ) )

print( bool( {1} ) )

print( bool( {1:1} ) )