'''
Here is the Python script that corresponds to the 23rd episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Control Flow is the order that statements and expressions 
are evaluated in a programming language.
Usually top down, left to right.
'''

# This comment is being ignored by Python.



'''
Arithmetic follows PEMDAS/BODMAS
'''

x = 1 + 3 - 4 * 2 + 6 # multiplication first, then the 
# addition and subtraction.

print(x)



'''
Exponents evaluate from right to left:
'''

ans = 2 ** 2 ** 3 # 64 or 256?

print(ans)



'''
We can use parentheses to control which expressions evaluate 
first
'''

ans = (2 ** 2) ** 3

print(ans)



'''
Parentheses can be used on more than arithmetic:
'''

condition = True ^ True and False

print(condition)

conditiion = True ^ (True and False)

print(condition)



'''
One more example:
'''

a = 'A'
b = 'B'

ans = a+b.lower()

print(ans)

ans = (a+b).lower()

print(ans)