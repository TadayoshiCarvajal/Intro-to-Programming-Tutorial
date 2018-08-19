'''
Here is the Python script that corresponds to the 17th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''



'''
Working with nested dictionaries is similar to working with multidimensional arrays
'''
outer_dict = {'dict1': {}, 'dict2': {}, 'dict3': {}} # A dictionary of dictionaries

# To access the third inner dictionary:
outer_dict['dict1']

# To add an item to the third inner dictionary:
outer_dict['dict1']['a'] = 'A'


print( outer_dict['dict1']['a'] )



'''
This can get pretty elaborate...
'''

dict_var = {'d1': { 'list1': [1, 2, 3, 4, ('one', 'two', 'three', 'four')] }}

'''
To access the letter 'u' in the string 'four' of the above dictionary
we need to use a combination of dictionary keying, list indexing, tuple indexing,
and string indexing.
'''

letter_u = dict_var['d1']['list1'][4][3][2] # the letter u

print( letter_u )



'''
Clear method - used to empty the contents of a dictionary
'''

dict_var = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6}

dict_var.clear() # delete all of the KV pairs



'''
To get the keys, values, and KV pairs of a dictionary
'''

dict_var = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6}

print( dict_var.keys() )

print( dict_var.values() )

print( dict_var.items() )



'''
To access the objects we can cast to list and index into the list
'''
print( list(dict_var.items())[0] ) # prints the first KV pair in dict_var



'''
Dictionaries also have a copy method that performs a shallow copy.
Shallow copy - copies object that is being copied. The internal objects are shared between both copies.
Deep copy - copies the internal objects as well. 
'''

d = {1:'one', 2:'two', 3:'three', 'keys': [1,2,3]}

e = d.copy() # a shallow copy of d.

print(d)

print(e)

d[2] = 'too'

print(d) # d has been changed

print(e) # e has not

d['keys'][0] = 'one'

print(d)

print(e) 



'''
Both dictionaries have had their internal lists modified. This is because with 
the shallow copy, the internal objects are shared between the two dictionaries.
'''