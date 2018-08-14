'''
Here is the Python script that corresponds to the 11th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Methods
All methods are functions. They are functions that are associated
with a specific type/class of object.

print is a function 
'''

print('1')
print(1)
print(1.0)

'''
To view str methods call dir on str
'''
print(dir(str))

'''
To use a method we use the dot operator
'''
string_var = 'capitalize me'
print(string_var.capitalize())

'''
We can't use capitalize on int because the int class doesn't implement
a capitalize method.
'''
int_var = 123
#int_var.capitalize() # This would throw an error


'''
We didn't change the value of string_var, we created a new
version of it.
'''
print(string_var)

'''
Lower and Uppercasing strings:
lower(arg) - lowercase all the letters of arg
upper(arg) - uppercase all the letters of arg
'''
string_var = string_var.upper()
print(string_var)

string_var = string_var.lower()
print(string_var)

'''
How can we get the # of times a substring occurs in a string?
'''
shakespeare = 'To be or not to? That is the question.'
t_count = shakespeare.count('t')
print(t_count)

'''
We can use method chaining to chain together multiple method calls.
Each call gets evaluated left to right. Use lower to lowercase 
shakespeare, then use count to count all of the t's lower and upper.
''' 
all_t_count = shakespeare.lower().count('t')
# 'to be or not to be? that is the question.'.count('t')
# 7
print( all_t_count )

'''
index(arg) - returns the index of the first occurence of arg.
'''
first_t = shakespeare.index('t') # returns 11
print(first_t)

'''
replace(arg1, arg2) - can be used to replace all of the occurences 
of arg1 with arg2.
'''
missing_t = shakespeare.lower().replace('t', '')
print(missing_t) # all of the t's removed from shakespeare

'''
strip(arg) - removes arg from the outsides(beginning or end) 
of the string
'''
print( 'strip the ! from the end !'.strip('!') )