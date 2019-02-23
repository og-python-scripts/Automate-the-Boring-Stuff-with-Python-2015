spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
['cat', 'bat', 'rat', 'elephant']
spam[1:3]
['bat', 'rat']
spam[0:-1]
['cat', 'bat', 'rat']

spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
['cat', 'bat', 'rat', 'elephant']
spam[1:3]
['bat', 'rat']
spam[0:-1]
['cat', 'bat', 'rat']
spam[:]
['cat', 'bat', 'rat', 'elephant']

spam = ['cat', 'dog', 'moose']
len(spam)
3


'''
Changing Values in a List with Indexes
Normally a variable name goes on the left side of an assignment statement,
like spam = 42. However, you can also use an index of a list to change
the value at that index. For example, spam[1] = 'aardvark' means “Assign the
value at index 1 in the list spam to the string 'aardvark'.” Enter the following
into the interactive shell:
'''

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
['cat', 'aardvark', 'rat', 'elephant']
spam[2] = spam[1]
spam
['cat', 'aardvark', 'aardvark', 'elephant']
spam[-1] = 12345
spam
['cat', 'aardvark', 'aardvark', 12345]

'''
List Concatenation and List Replication
The + operator can combine two lists to create a new list value in the same
way it combines two strings into a new string value. The * operator can also
be used with a list and an integer value to replicate the list. Enter the following
into the interactive shell:
'''
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']

'''
Removing Values from Lists with del Statements
The del statement will delete values at an index in a list. All of the values
in the list after the deleted value will be moved up one index. For example,
enter the following into the interactive shell:
'''
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
