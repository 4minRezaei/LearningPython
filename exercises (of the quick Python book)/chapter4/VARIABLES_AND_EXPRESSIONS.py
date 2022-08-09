'''
In the Python shell, create some variables. What happens when you try to put spaces, dashes,
or other nonalphanumeric characters in the variable name? Play around with a few complex
expressions, such as x = 2 + 4 * 5 - 6 / 3. Use parentheses to group the
numbers in different ways and see how the result changes compared with the
original ungrouped expression
'''
x =  
print(x)
# output: SyntaxError: invalid syntax

x = -
print(x)
# output: SyntaxError: invalid syntax

x = &
print(x)
# output: SyntaxError: invalid syntax

x = 2 + 4 * 5 - 6 / 3
print(x)
# output: 20.0

x = (2 + 4) * 5 - 6 / 3
print(x)
# output: 28.0

x = 2 + 4 * (5 - 6) / 3
print(x)
# output: 0.6666666666666667