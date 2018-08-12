'''
Here is the Python script that corresponds to the 8th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Let's learn about strings!
The string class is abbreviated to str in Python.
'''

'''
Literals
Literals are the literal values that we assign to variables.
You can either assign a variable or a literal to a variable.
(Later when we learn about objects, you will learn to assign object
constructors to variables as well).
'''

int_var = 435 # 435 is and integer literal representing the value 435

float_var = 36.5 # the floating point literal with value 36.5

a = 6
b = 7
var1 = a + b + 4

'''
The string class has a few literals:
'''
# Single line string literals
str_literal_1 = 'This is a string declared using single quotes'
print(str_literal_1)

car1 = 'Ford Focus'
print(car1)

str_literal_2 = "This is a string declared using double quotes"
print(str_literal_2)
car2 = "Toyota Camry"
print(car2)

#Multiline string literals:
multi_line_str1 = '''This is the first way to declare a 
multiline string'''
print(multi_line_str1)

multi_line_str2 = """This
is
the
second
way
to
declare
one"""
print(multi_line_str2)

multi_line_str3 = "This is the thirds \
way to write a string that spans multiple lines."
print(multi_line_str3)

'''
Why so many ways to declare a string? Flexibility
'''
# We can declare using single quotes if we expect the string will contain double quotes
example_str1 = 'This is a string with a nested double quote: "Mary had a little lamb", said the man'
print(example_str1)

# We can declare using double quotes if we expect the string will contain double quotes
example_str2 = "This is a string with an apostrophe: Yoshi's videos are awesome. He's also a humble dude :P"
print(example_str2)

# We can also mix these using backslash character
example_str3 = '''Using the escape character (backslash) we can have both inner quotes and apostrophes: 
""Yoshi\'s weird for referring to himself in the third person"-Yoshi"-Michael Scott.'''
print(example_str3)

'''
We can combine strings using concatentation. The concatenation operator is the + symbol (like arithmetic addition)
'''
firstName = 'Jon'
lastName = 'Snow'
fullName = firstName + lastName
print(fullName) # 'JonSnow' to fix this we should include a ' ' in the concatenation.

fullName = firstName + ' ' + lastName
print(fullName)