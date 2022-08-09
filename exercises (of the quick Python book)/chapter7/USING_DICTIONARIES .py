'''
Suppose that you're writing a program that works like a spreadsheet.
How might you use a dictionary to store the contents of a sheet?
Write some sample code to both store a value and retrieve a
value in a particular cell. What might be some drawbacks to this approach?
'''

table = dict()
ext = ''

while (ext != 'done'):
    row = int(input('Enter Row number please:\n'))
    column = int(input('Enter column number please:\n'))
    val = input('Enter value please:\n')
    table[(row, column)] = val
    ext = input('Enter Done if you\'re done, otherwise hit Enter.\n').lower()

ext = ''
while (ext != 'done'):
    row = int(input('Enter Row number that you\'re looking for please:\n'))
    column = int(input('Enter column number that you\'re looking for please:\n'))
    print('\nThe value in row {0} and column {1} is: '.format(row, column), table[(row, column)])
    ext = input('Enter Done if you\'re done, otherwise hit Enter.\n').lower()