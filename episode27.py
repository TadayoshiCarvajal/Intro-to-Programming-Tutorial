'''
Here is the Python script that corresponds to the 27th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
Iteration - repetition of programming instructions
Iterable - an object which implements an __iter__ method
Iterator - an object which can be used in a for-loop to do repeat work
'''



iterator = [1,2,3,4,5,6,7,8,9,10]

'''
We declare a for-loop as such:
'''

for i in iterator:
    print(i) # print each value of i in the iterator




'''
What if we want to do work that repeats 10000 times?

Use the range function to return an iterator containing values in the specified 
range
'''

list_var = []

for i in range(10000):
    list_var.append(i)

print(list_var)