'''
Explain why the following operations aren't legal for the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
'''
x = (1, 2, 3, 4)

x.append(1)
# output: AttributeError:
# 'tuple' object has no attribute 'append'

x[1] = "hello"
# output: TypeError:
# 'tuple' object does not support item assignment

del x[2]
# output: TypeError:
# 'tuple' object doesn't support item deletion


'''
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?
'''
x = (3, 1, 4, 2)
x = list(x)
x.sort()
x = tuple(x)
print(x)
# output: (1, 2, 3, 4)
