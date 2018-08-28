'''
Here is the Python script that corresponds to the 26th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''

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

        odd_number = int(num) % 2 # 1 if odd, 0 if even
        if odd_number and int(num) != 1: # implicitly evaluate odd_number
            print('odd')
        elif not odd_number:
            print('even')
    else:
        print('The number was not in the range 1 - 100')
else:
    print('Must enter an integer')



'''
Many types in python evaluate implicitly as booleans:
'''

user_input = input('Type something: ').strip()

if user_input: # if the string is not empty
    print('You typed: ', user_input)
else: # if the string is empty
    print('You didn\'t type anything')



'''
Short circuit evaluation
With boolean expressions, Python is sometimes able to perform shortcuts with the 
evaluation of the boolean. For example, we know that AND is only true, if both of its 
arguments are True. Therefore, if the first argument is False, Python knows right away
that even if the second argument is True, the expression as a whole will evaluate to 
False, because AND requires that both of its arguments are True for it to evaluate as 
True. So Python doesn't even look at the second argument of the AND operator if it sees 
that the first argument is False.

Similarly for OR, we know that the expression involving an OR operator is True so long 
as 1 of its arguments is True. So if we check the first argument and see that it is 
True, we don't even check the second, we can assume that the argument as a whole will 
evaluate to True.
'''

if False and True: # the True in this expression isn't even looked at
    print('AND short circuited')

if True or False: # the False in this expression isn't even looked at
    print('OR short circuited')



'''
Original example using short circuit evalutation.
'''

num = input('Enter an integer: ').strip()

if num.isdigit() and 1 <= int(num) <= 100:# short circuits if the first arg is False.
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

    odd_number = int(num) % 2 # 1 if odd, 0 if even
    if odd_number and int(num) != 1:
        print('odd')
    elif not odd_number:
        print('even')
elif num.isdigit():
        print('The number was not in the range 1 - 100')
else:
    print('Must enter an integer')