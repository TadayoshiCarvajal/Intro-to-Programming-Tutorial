'''
Here is the Python script that corresponds to the 7th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Incrementation (aka Augmented Assignment)
'''
apples = 0
print(apples)
apples += 1 # same as apples = apples + 1
print(apples)
apples += 1
print(apples)
apples *= 2
print(apples)
apples /= 2
print(apples)
apples %= 2
print(apples)
apples ** 2
print(apples)
apples //= 2
print(apples)

'''
Unit 1 Review:
Let's review the concepts we've learned so far in this unit.
The concepts discussed are:
-- Variables
-- Assignment
-- Arithmetic
-- Modules
-- Dot operator
-- Some basic functions (print, dir, help, sqrt, etc.)
'''

'''
a) Create 3 variables: a, b, and c. Assign 3 to a, 4 to b,
and assign the square root of (a^2 + b^2) to c.
'''
a = 3
b = 4
c = (a**2 + b**2)**0.5
print(a)
print(b)
print(c)

'''
b) What are the types of a, b, and c?
'''
print(type(a))
print(type(b))
print(type(c))

'''
c) Create a variable d, and initialize it with the value
of the integer version of c.
'''
d = int(c)
print(c)

'''
d) Type cast the values of a and b to floats and store
them in variables e and f, respectively.
'''
e = float(a)
f = float(b)
print(a)
print(b)

'''
e) Create a variable g, and assign the value of
the (square root of e * f)*pi, using the math module.
'''
from math import sqrt, pi
g = sqrt(e*f) * pi
print(g)

'''
f) Increment g by 100
'''
g += 100
print(g)