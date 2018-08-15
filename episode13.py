'''
Here is the Python script that corresponds to the 13th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Lists are sequences (positionally ordered collections of objects)
Lists are heterogenous (support multiple object types)
Lists, like strings, use zero-based indexes.
'''
list_var = [1, 1.0, 'one']


'''
Lists are dynamic
'''
list_var.append( [] ) # this is how we add elements
list_var.remove( [] ) # this is how remove elements


'''
Indexing
'''
list_var[0]  #first element
list_var[-1] #last element
#list_var[-len(list_var)-1] # This causes an index error


'''
Slicing
list[start:stop:step]
'''
list_var[:2]
list_var[::-1] # reversed a list.


'''
Use reversed to reverse a sequence.
'''
reversed(list_var) # returns an iterator object. Cast to list.


'''
Reverse in place:
'''
list_var.reverse() # now list_var is reversed


'''
Concatenation:
'''
list_var2 = [2, 2.0, 'two']
list_var + list_var2


'''
Index method to get the index of an element. 
'''
list_var.index('one')


'''
Count method to get the # of occurences of an element.
'''
new_list = [1,1,1,1]
new_list.count(1) #4