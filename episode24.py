'''
Here is the Python script that corresponds to the 24th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''



'''
if statements:
'''
if True:
    # do stuff
    pass # we'll talk about what this does later.



'''
Indentation matters in python.
We can use any amount of indentation but you must be consistent:
'''

if True:
    print('True')
    # print('Inconsistent') # This would cause an error because
    #  we are using inconsistent indentation.



'''
Example 1:
'''

a = 1
condition = True

if condition:
    a = 2
    print('The condition was True.')

print('a =', a)



'''
Example 2:
'''

a = 1
condition = False

if condition:
    a = 2
    print('The condition was True.')

print('a =', a)



'''
We can use elif for multiple conditions:
Example 3:
'''

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'

traffic_light = RED

if traffic_light is GREEN:
    print('Go!')
elif traffic_light is YELLOW:
    print('Slow down!')
elif traffic_light is RED:
    print('Stop!')



'''
When one condition is true, we exit the conditional block entirely!
Example 4:
'''

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'

traffic_light = RED

if traffic_light is GREEN:
    print('Go!')
elif traffic_light is YELLOW:
    print('Slow down!')
elif traffic_light is RED:
    print('Stop!')
elif traffic_light is RED:
    print('Will this get printed?')



'''
conditional blocks can also include an else statement. Else is a 
catch-all condition. If none of the conditions before the else 
are activated, the else block will run.
'''

traffic_light = 'BROKEN'

if traffic_light is GREEN:
    print('Go!')
elif traffic_light is YELLOW:
    print('Slow down!')
elif traffic_light is RED:
    print('Stop!')
elif traffic_light is RED:
    print('Will this get printed?')
else:
    print('The light is broken! Be careful!')