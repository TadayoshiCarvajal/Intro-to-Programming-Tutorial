'''
Here is the Python script that corresponds to the sixth episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Modules allow us to access prewritten code so we don't have to reinvent the 
wheel everytime we want to make something. To use a module we import it via
the import statement.
'''
import math

'''
The dir function allows us to explore the contents of a file.
Use dir on math to view the functions and variables available in math
'''
print(dir(math))

'''
To access the contents of the math class, we must use the dot operator
'''
print( math.pi )

'''
If we use dir without passing arguments to it, we can view the contents
of the current environment
'''
print( dir() )

'''
To view the functions that are built-in, we can use dir on the __builtins__
'''
print(dir(__builtins__))

'''
Python supports three ways to calculate a square root

Method #1: using the arithmetic operator for exponents
'''
print( 16 ** 0.5 )
print( 8 ** (1/3) )

'''
Method #2: using the builtin pow function
'''
print( pow(16, 0.5) )
print( pow(8, 1/3) )

'''
Method #3: using the math module's sqrt function
'''
print( math.sqrt(16) ) # Note: We there is not a cubic root function in math

'''
To import sqrt into our environment, use from
'''
from math import sqrt

print(sqrt(16))

'''
To import all of the contents of a module, use *
'''
from math import *