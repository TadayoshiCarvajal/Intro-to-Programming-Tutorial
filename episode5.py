'''
Here is the Python script that corresponds to the fifth episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Hey guys! :D
Let's learn about type casting and some more
arithmetic.
'''

'''
2 ^ 3 = 2 * 2 * 2 = 8
'''

'''
2 ^ 100 = 2 * 2 * 2 * ... * 2 * 2 = 
1267650600228229401496703205376
'''

'''
exponents are denoted with ** symbol:
'''
exponent_var = 2 ** 3
print('2 ^ 3 =')
print(exponent_var)

'''
Modulus gives us the remainder:
'''
modulus_var = 5 % 2
print('5 % 2 =')
print(modulus_var)

'''
Floor Division aka Integer Division
gives us the whole number division:
'''
floordiv_var = 5 // 2
print('5 // 2 =')
print(floordiv_var)

'''
negation example:
'''
a = 34
print('-a')
print(-a)

'''
Implicit Type Casting:
'''
implicit_var = 1 * 3 + 5 - 7 * 3.5
print('1 * 3 + 5 - 7 * 3.5 = -16.5')
print(implicit_var)

'''
Explicit Type Casting
'''
answer = int(10/2)
print(answer)

c = 10/2
a = 3 + int(c)
print(a)