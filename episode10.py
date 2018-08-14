'''
Here is the Python script that corresponds to the 10th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

firstName = 'Jon'
lastName = 'Snow'
fullName = firstName + ' ' + lastName

'''
Duplication
Let's say that we want to repeat a string many times.
If we do this manually it would take a long time.
'''
num1 = '12345678910' 
print(example_str * 1000)

'''
Casting from string to int
'''

num1_int = int(num1)
print(num1_int)

'''
Casting from string to float
'''
num2 = '3.14159'
num2_float = float(num2)
print(num2_float)

'''
# This causes an error because we cannot evaluate 'a' as a number
num3 = '12345a'
'''

'''
We can also go from float and int back to str
'''
a = 1000
a_str = str(a)
print(a_str)

'''
Slicing let's us get parts of a string by slicing the string that's
being sliced from a starting index to an ending index.

identifier[start:stop] *start goes up to but not including this index.

''' 

jon = fullName[0:3]
snow = fullName[4:8]
print(jon)
print(snow)

'''
We can shorten this because start and stop default to 0
and the len(identifier), respectively. 
'''
jon_otherway = fullName[:3]
snow_otherway = fullName[4:]

print(jon_otherway)
print(snow_otherway)

'''
slicing also takes an optional third parameter, step.
identifier[start:stop:step] *step controls how we increment to 
get the indeces in the string slice and defaults to 1.
'''
everyother = fullName[::2]

print(everyother)

'''
We can also use negative step values to reverse our string.
'''
backwards = fullName[::-1]

print(backwards)