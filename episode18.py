'''
Here is the Python script that corresponds to the 18th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Let's learn about sets!
'''



'''
What is a set? A set is a collection of unique elements.
'''

A = {1,2,3,4,5} # a set literal assigned to the variable A

B = {4,5,6,7,8} 

C = set() # the empty set literal



'''
To access the elements of a set by position, convert to a list first.A
'''

print( list(A)[0] ) # this prints the first item in the A



'''
We can convert a list to a set to remove duplicate entries.
'''

list_var = [1,1,1,2,2,3,4,4,4,5,5,6]

print( set(list_var) ) # prints the unique elements of list_var



'''
Intersection: the elements that exist in both A and B.
Symbol : &
'''

ans = A & B

print('A & B',ans)



'''
Union: the elements that exist in A or B or both.
Symbol : |
'''

ans = A | B

print('A | B',ans)



'''
Difference: the elements the exist in A but not in B.
Symbol: -
'''

ans1 = A - B
ans2 = B - A
print('A - B =',ans1, 'B - A', ans2)



'''
Symmetric Difference: the elements in either A or B but not in both.
Symbol: ^
'''

ans = A ^ B

print(ans)



'''
Set methods:
'''

D = A | B

print('D = A|B = ', D)

D.clear()

print('D.clear() = ', D)

D = A.copy() # a shallow copy of A

print('D = A.copy()', D)



'''
set operators are also methods:
'''

print('A.difference(B) = ',A.difference(B), '(this is the same as A - B)')

















































'''
We can also do augmented assignment for set operations like we did for arithmetic.B
'''

A.difference_update(B) # ===  A-= B  ==  A = A - B (all three do the same thing)

print(A)