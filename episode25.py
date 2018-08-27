'''
Here is the Python script that corresponds to the 25th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''


''' 
We can use compound boolean expressions to make more complex conditions 
in conditional blocks:
'''

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'

traffic_light = RED

if traffic_light is GREEN:
    print('Go!')
elif traffic_light is YELLOW:
    print('Slow down!')
elif traffic_light is RED and traffic_light is not GREEN and traffic_light is not YELLOW:
    print('Stop!')


'''
Read input from the user. Assume only integers between the range of 0-100 inclusive 
will be given. 90 and above earn an A, 80 and above earn a B, 70 and above earn a C, 
65 and above earns a D. Anything below a 65 earns an F. Print the letter grade.
'''

'''
Attempt #1:
'''

grade = input('Enter grade: ')
grade = int(grade) # input always returns str so we convert to int to compare below

if grade >= 0:
    print('F')
if grade >= 65:
    print('D')
if grade >= 70:
    print('C')
if grade >= 80:
    print('B')
if grade >= 90:
    print('A')

'''
Attempt #2:
'''

grade = input('Enter grade: ')
grade = int(grade)

if grade >= 0:
    print('F')
elif grade >= 65:
    print('D')
elif grade >= 70:
    print('C')
elif grade >= 80:
    print('B')
else:
    print('A')

'''
Attempt #3:
'''

grade = input('Enter grade: ')
grade = int(grade)

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 65:
    print('D')
else:
    print('F')



'''
We can also nest expressions. For example read a number from the user using input.
Input returns a string. Test if the string that the user entered represents an integer. 
If it is, print the place of the number. If it's not, print 'Must enter an integer':

Example: 1 is numeric so we would print 
    1st
Example: 4.5 is not an integer:
    Must enter an integer
'''

num = input('Enter an integer: ').strip() # we strip to remove white space before & after
if num.isdigit():
    last_digit = int(num[-1])
    if last_digit == 1 and num != '11':
        suffix = 'st'
    elif last_digit == 2 and num != '12':
        suffix = 'nd'
    elif last_digit == 3 and num != '13':
        suffix = 'rd'
    else:
        suffix = 'th'
    print(num + suffix)
else:
    print('Must enter an integer')



'''
We can even nest conditional blocks inside of conditional blocks inside of conditional 
blocks. There is no limit to conditional nesting although you should start to think 
about the readability of your code after 3 or more indents. The least complex effective 
solution is always the best. In the previous example, 
    if the user enters a number greater than 100 or less than 1:
        The number was not in the range 1 - 100
    if the number is 1, type 
        You win! 
        1st
    if the number is odd, and not 1, print 'odd' after the place
    if the number is even, print 'even' after the place
'''

num = input('Enter an integer: ').strip()

if num.isdigit():
    if 1 <= int(num) <= 100:
        last_digit = int(num[-1])
        if last_digit == 1 and num != '11':
            suffix = 'st'
        elif last_digit == 2 and num != '12':
            suffix = 'nd'
        elif last_digit == 3 and num != '13':
            suffix = 'rd'
        else:
            suffix = 'th'
        print(num + suffix)
    
        if num == '1':
            print('You win!')

        odd_number = int(num) % 2 == 1 # True if the number is odd, False if even.
        if odd_number and int(num) != 1:
            print('odd')
        elif not odd_number:
            print('even')
    else:
        print('The number was not in the range 1 - 100')
else:
    print('Must enter an integer')