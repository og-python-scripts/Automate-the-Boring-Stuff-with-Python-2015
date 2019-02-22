'''There are some values in other data types that conditions will consider equivalent
to True and False. When used in conditions, 0, 0.0, and '' (the empty
string) are considered False, while all other values are considered True. For
example, look at the following program:'''

name = ''
while not name:u
  print('Enter your name:')
  name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:v
  print('Be sure to have enough room for all your guests.')w
print('Done')

'''If the user enters a blank string for name, then the while statement’s condition
will be True u, and the program continues to ask for a name. If the value for
numOfGuests is not 0 v, then the condition is considered to be True, and the
program will print a reminder for the user w.
You could have typed not name != '' instead of not name, and numOfGuests
!= 0 instead of numOfGuests, but using the truthy and falsey values can make
your code easier to read.'''
