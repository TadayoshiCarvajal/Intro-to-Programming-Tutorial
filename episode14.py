'''
Here is the Python script that corresponds to the 14th episode in
my YouTube tutorial series, Intro to Programming in Python.
Follow me at KaizenMachina on YouTube for daily content.
'''


'''
How to convert from list of strings to a string?
'''
fawkes = ['Remember', 'remember', 'the', 'fifth', 'of', 'November...']

attempt1 = str(fawkes)

print(attempt1) # This is not quite what we wanted...



'''
Use join to join strings separated by a specified string:
'''
attempt2 = ' '.join(fawkes)

print(attempt2) # 'Remember remember the fifth of November...'



'''
What if we have non strings in the list?
'''
list_tostring = ['This is a', 'list containing', 'the numbers:',1,2,3,4,5]

#print( ' '.join(list_tostring) ) # this causes an error.
# The above list contains ints as well as string. We should use map

print( ' '.join( list( map( str, list_tostring ) ) ) )



'''
Going from string to list:
'''
string_var = 'Going from string to list'

attempt1 = list(string_var) # this gives us a list of characters.

print(attempt1) 



'''
Use split to get a list of words.
'''
attempt2 = string_var.split()

print(attempt2)



'''
The split method's arg is the delimiter, aka separating character
by which we are splitting the string up. It defaults to white space.
'''
ip = '123.45.67.89'

ip_split = ip.split('.')

print(ip_split)



'''
Multidimensional lists
'''
tictactoe = [['o','o','x'],
             ['x','x','o'],
             ['x','o','x']]

print(tictactoe)

print( tictactoe[1][1] ) # the middle square in tic-tac-toe



'''
Getting dimensions:
    If the board is square like it is in tic-tac-toe, then # rows = # columns:
'''
n_rows = len( tictactoe )

n_cols = n_rows



'''
If the board is rectangular, we can also use n_cols = len(board[0])
'''
rect_board = [[1,2,3,4,5],
              [1,2,3,4,5],
              [1,2,3,4,5],
              [1,2,3,4,5]]

n_rows = len( rect_board )     
n_cols = len( rect_board[0] )



'''
A 3D list is really a list of 2D lists.
*** So a 3D list can represent the moves of an entire game.***
'''                       
list_3D =   [
             [[' ',' ',' '],
              [' ','x',' '],
              [' ',' ',' ']],

             [['o',' ',' '],
              [' ','x',' '],
              [' ',' ',' ']],
              
             [['o',' ',' '],
              [' ','x',' '],
              [' ',' ','x']]
            ]



'''
A 4D list is really a list of 3D lists.
*** A 4D list can represent the moves over many games ***
'''
list_4D = [
            [
             [[' ',' ',' '],
              [' ','x',' '],
              [' ',' ',' ']],

             [['o',' ',' '],
              [' ','x',' '],
              [' ',' ',' ']],
              
             [['o',' ',' '],
              [' ','x',' '],
              [' ',' ','x']]
            ],

            [
             [[' ',' ',' '],
              [' ','x',' '],
              [' ',' ',' ']],

             [[' ',' ','o'],
              [' ','x',' '],
              [' ',' ',' ']],
              
             [['x',' ','o'],
              [' ','x',' '],
              [' ',' ',' ']]
            ]
        ]