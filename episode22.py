'''
Here is the Python script that corresponds to the 22nd episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''



print( [1,2,3] == [1,2,3] ) # True, these lists contain the same values.

print( {1,2,3,4} != {2,4,5,6} ) # True, these sets are not equivalent.

print( 123 == 123 ) # True, these ints are the same value.



'''
Python has another operator: is
is tests whether two references (variables) or objects are the same 
object in memory.
'''

print( [1,2,3] is [1,2,3] ) # This is False (2 different list objects)



'''
When working on small ints and strings, python caches the objects 
for reuse.
'''

print( 123 is 123 ) # True, these ints are the same objects in memory.

a = 'Danaerys'
b = 'Danaerys'

print( a is b ) # True, python cached the string 'Danaerys' for reuse.



'''
Shallow copies share internal objects:
'''

dragons = [ ['Drogon', 'Viserion', 'Rhaegal'] ]

dragons_copy = dragons.copy()

print(dragons is dragons_copy) # False, copy is a new list object.

print(dragons[0] is dragons_copy[0]) # True, the copy was shallow, 
#so the internal objects are the same in both.



'''
You can also use not with is to check if an object is not another 
object
'''

Lannister = {'Tyrion', 'Cersei', 'Jaime'}

Stark = {'Bran', 'Arya', 'Sansa', 'Rob', 'Rickon'}

print( Lannister is not Stark ) # True these are different objects.



'''
Use == to compare values are the same, use is to compare objects 
are the same.
'''


'''
Review Questions:
Solve these in your head first and then run the code snippets 
to test if you were right.
'''

# 1) What is ans at the end of this code?
ans = 'S'

to_add = list('olution')

ans += to_add[0]
ans += to_add[1].upper()
ans += to_add[2]
ans += to_add[3].upper()
ans += to_add[4]
ans += to_add[5].upper()
ans += to_add[6]

print(ans)



# 2) What is ans at the end of this code?
ans = ('Almost', '_', 'there!', '_', 'Keep', '_', 'it', '_', 'up!')

ans = ' '.join( ans[::2] )

print(ans)



# 3) What is ans at the end of this code?
A = {'Facebook', 'Google', 'Amazon', 'Apple', 'Microsoft'}

B = {'Facebook':1, 'Google':2, 'Amazon':3, 'Apple':4, 'Microsoft':5}

ans = (set( B.keys() ) is A) ^ (set( B.keys() ) == A)

print(ans)



# 4) What is ans at the end of this code?

ans = not not not not not not not not not True

print(ans)



# 5) What is ans at the end of this code? 
# Hint: chr does the opposite of ord, it converts from ordinal back 
# to character.
''' Hint 2:
    A - 65
    B - 66
    C - 67
    D - 68
    E - 69
    F - 70
    G - 71
    H - 72
    I - 73
    J - 74
    K - 75
    L - 76
    M - 77
    N - 78
    O - 79
    P - 80
    Q - 81
    R - 82
    S - 83
    T - 84
    U - 85
    V - 86
    W - 87
    X - 88
    Y - 89
    Z - 90
    ! - 33
    . - 46
'''

encrypt = '33,46,69,46,78,46,79,46,68,46,76,46,76,46,65'
encrypt = list(map(int,encrypt.split(',')))
inter = ''.join( list( map( chr, encrypt[0::2]) ) ).lower()
ans = (inter[:5] + ' ' + inter[5:])[::-1].capitalize()

print(ans)