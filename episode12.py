'''
Here is the Python script that corresponds to the 12th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Escape characters begin with \
Examples: 
    \n
    \t
'''
print('\thello')
print('\nworld\n')

'''
Print can take multiple space separated arguments.
'''
print(3)
print('three')
print(3, 'three') # '3 three' 

'''
To control how we separate the comma separated arguments, specify
the sep keyword argument sep:
'''
print(3, 'three', sep=',')

'''
We can also control what each print function call ends with by
specifying the keyword argument end as well. It is \n by default.
'''
print(3, 'three', sep=',', end='~~')
print()

jordans = 121.99
count = 3
total = count * jordans
'''
How do we print something like:
    Jordans (3x121.99)=365.97
'''
concat = '\tJordans (' + str(count)+'x'+str(jordans)+')='+str(round(total,2))
print(concat)

'''
Use round to round the value of total to 2 decimal places:
'''
concat2 = '\tJordans (' + str(count)+'x'+\
str(jordans)+')='+str(round(total,2)) # nested function call

print(concat2)
'''
Another way is using string formatting
Important: pay attention to # of open and close parenthesis when
nesting function calls.
'''
formatted = '\tJordans ({}x{})={}'.format(count, jordans, round(total,2))
print(formatted)

'''
New way to format strings, use f
'''
formatted = f'\tJordans ({count:d}x{jordans:f})={round(total,2):f}'