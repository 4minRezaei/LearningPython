'''
 If you wanted to check whether a line ends
with the string "rejected", what string method would you use?
Would there
be any other ways to get the same result?
'''
x = 'If you wanted to check whether a line ends with the string rejected'
print(x.endswith('rejected'))

if x.count('rejected', -8) > 0:
    print('True')
else:
    print('False')
