'''
Here is the Python script that corresponds to the 21st episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Compound Boolean statements
'''

'''
Compound boolean operators: and, or, xor
'''

'''
AND Truth Table
  A  |  B  | A and B
--------------------
  T  |  T  |   T
  T  |  F  |   F
  F  |  T  |   F
  F  |  F  |   F
'''
'''
OR Truth Table
  A  |  B  | A or B
--------------------
  T  |  T  |   T
  T  |  F  |   T
  F  |  T  |   T
  F  |  F  |   F
'''
'''
XOR Truth Table
  A  |  B  | A xor B
--------------------
  T  |  T  |   F
  T  |  F  |   T
  F  |  T  |   T
  F  |  F  |   F
'''



'''
In Python,
    and = and 
    or = or
    xor = ^
'''
print(True and True)

print(False or True)

print(True ^ False)



x = 2
y = 4
'''
consider the expression:
    bool(x < 3 < y) and bool(x)
    
    (evaluate the left hand side first...)
        2 < 3 < 4 = True

    True and x

    (evaluate the right hand side...)

        x = 2 = True (because its not zero)

    True and True

    (Both True is True according to the and truth table)

'''
print(bool(x < 3 < y) and bool(x))



'''
consider the expression:
    bool([]) or bool(())
    
    (evaluate the left hand side first...)
        [] = False (because its empty)

    False or ()

    (evaluate the right hand side...)

        () = False (because its empty)

    False or False

    (Both False is False according to the OR truth table)

'''
print( bool([]) or bool(()) )



x = 2
y = 3
'''
consider the expression:
    bool(x - y) ^ bool({1,2,3} > {1,2,3})
    
    (evaluate the left hand side first...)
        2 - 3
        -1 = True (because its not zero)

    True ^ {1,2,3} > {1,2,3}

    (evaluate the right hand side...)

        {1,2,3} > {1,2,3} = False (because its not a proper superset)

    True ^ False

    (True ^ False is True according to the XOR truth table)

'''
print(  bool(x - y) ^ bool({1,2,3} > {1,2,3}) )



'''
Methods containing the word 'is' are usually methods that return 
a boolean value. 
Example: The string class's isalpha method
'''
print( 'alphabet'.isalpha() ) # true because the string only contains alpha chars

'''
Last example:

not (not (True and False) and 'Jon Snow'.isalpha() and (1 in [0, [1,2,3]] or []) ) 

    Evaluate the innermost level of parenthesis:

        not(not(False) and 'Jon Snow'.isalpha() and (False or False))
    
        not(True and 'Jon Snow'.isalpha() and False)

    Evaluate non boolean expressions in the innermost level of parenthesis:

        not(True and False and False)

    Evaluate the multiple compound boolean expression from left to right:

        not(False and False)

        not(False)

    Finally not False = True

        True
'''
val = not (not (True and False) and 'Jon Snow'.isalpha() and (1 in [0, [1,2,3]] or []) ) 

print( val )