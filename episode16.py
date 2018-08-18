'''
Here is the Python script that corresponds to the 16th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Dictionary is a collection of key-value pairs (KV pairs).
KV pairs are pairings of a key, and value.
Value is typically the important information we want to store,
and Key is the label we use to access that value from the dictionary.
Dictionary Literal:
'''
# KV Pairs are comma separated inside of curly braces.
dictionary = {'zebra':'an African wild horse with black-and-white stripes and an erect mane.'} 

print( dictionary['zebra'] )



'''
Keys must be hashable types. For now, only use immutable objects as keys.
'''
#dictionary2 = { [1,2,3]:'list containing 1, 2, & 3.' } # would cause an error because lists are not hashable.

dictionary2 = {tuple([1,2,3]):'this will work'}

print(dictionary2)



'''
To add items:
'''
dictionary2['second key'] = 'second value'

dictionary2['third key'] = 'third value'



'''
Keys must be unique
'''
dict1 = {1:'one', 2:'two', 3:'three', 4:'four'}

print( dict1 ) # the original dict1

dict1[1] = 'one replaced'

print( dict1 ) # still has 4 KV pairs. The first has been changed.



'''
Use del to remove KV Pairs from the dictionary.
'''
del dict[1]

print( dict1 )

print( dict1[1] ) # This would cause an error because that KV pair has been deleted.



'''
Del works on other mutable types as well
'''
list_var = [1,2,3,4,5]

del list_var[0] 

print( list_var )



'''
Del also works on variables
'''

one = 1.0

del one

print( one ) # this causes a NameError since one is no longer a reference. (we freed it)