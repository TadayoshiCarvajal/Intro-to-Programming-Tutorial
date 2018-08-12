'''
Here is the Python script that corresponds to the 9th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

'''
From the last video:
'''
firstName = 'Jon'
lastName = 'Snow'
fullName = firstName + ' ' + lastName

'''
Sequences are a positional ordering of elements.
'Jon' is NOT the same as 'Noj' or 'ojN'!
How do we access the various elements (characters) of a string?
Answer: Indexing
'''
print(fullName[0])
print(fullName[1])
print(fullName[2])
print(fullName[3])
print(fullName[4])
print(fullName[5])
print(fullName[6])
print(fullName[7])

'''
We use the len functio to get the length of a sequence (# of elements)
'''
print(len(firstName))
print(len(lastName))
print(len(fullName))

long_word = 'supercalifragilisticexpialidocious'
print(len(long_word))

'''
Use length of the string to access the last index:
'''
print(long_word[len(long_word) - 1])
#fullName[len(fullName)] #this will give us an error since 8 is out of bounds.

'''
long_word[len(long_word) - 1] this is pretty tedious
a more concise way is to use negative indexes.

long_word[len(long_word) - 1] is the same as long_word[-1]
'''
print(long_word[-1])

#fullName[-len(fullName)-1] #this will give us an error since -1 is out of bounds.