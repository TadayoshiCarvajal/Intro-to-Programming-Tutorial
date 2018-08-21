'''
Here is the Python script that corresponds to the 19th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Sets only support hashable types:
'''

# {[1,2,3]} # this returns an error because the list is not a hashable type



'''
Let's learn about booleans!
Literals: True or False
'''

a = True

b = False



'''
Use the in operator to check if item A is in collection B
'''
cat = 'cat'

seuss = 'The Cat in the Hat'

print(cat in suess) # this is False

print(cat in seuss.lower()) # this is True



'''
In works on all of the collection types we've seen
'''

list_var = [1,2,3,4,5]

tuple_var = (5,6,7,8,9)

print(5 in list_var, 5 in tuple_var) # both are True. 5 is in both of the sequences.

color = 'red'

colors = {'red', 'blue', 'green'}

print(color in colors) # True since 'red' is in the set.




'''
For dictionaries, in checks if item A is a key in dictionary B.
'''
cars = {
        'Ford': ['F150', 'Focus', 'Fusion'],
        'Toyota':['Corolla', 'Camry'] 
        }

print('Ford' in cars) # True since Ford is a key in the dictionary

print('Camry' in cars) # False since Camry is not a key in the dictionary

print('Camry' in cars['Toyota']) # Same as 'Camry' in ['Corolla', 'Camry']. True



'''
We can negate booleans by using the not operator.
'''

print(not True)

print(not False)



'''
We can also negate the in operator
'''

print('a' not in 'aeiou')

print(1 not in [2,4,6,8,10])

print('yellow' not in colors)

print('Ford' not in cars)



'''
Note: Make sure that in the expression: A in B, B is iterable or you will get a 
type error:
'''

#print(1 in 123)#this gives a type error because ints are not iterable.



'''
Python also has comparison operators: <, >, ==, >=, <=, !=.
'''

print(1 < 100) # True

print(2 > 1) # True

print(1 == 1.0) # True. Python converts the int 1 to 1.0 then compares 1.0 == 1.0 = True

print(2 >= 2) # True

print(6 <= 5) # False

print(10 != 10) # False



'''
We can chain multiple comparisons
'''
x = 5.0

y = 12

print(1 <= x <= 10 <= y <= 20) # True