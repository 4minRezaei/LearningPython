
a = "Hello"
b = "Amin"
c = 17
d = 98.47
e = (4+7j)

# what happens when you do operations with them, including across types?
a + b
'HelloAmin'

c * d
1673.99

e / c
(0.23529411764705882+0.4117647058823529j)

d // c
5.0

d / c
5.79235294117647

a * c
'HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello'

b + d
# output: Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     b + d
# TypeError: can only concatenate str (not "float") to str

b + c
# output: Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
#     b + c
# TypeError: can only concatenate str (not "int") to str

e * c
(68+119j)

# Load the math module and try a few of the functions.
import math
math.e
2.718281828459045

c + (2^math.e)
# output:Traceback (most recent call last):
#   File "<pyshell#19>", line 1, in <module>
#     c + (2^math.e)
# TypeError: unsupported operand type(s) for ^: 'int' and 'float'

c + (2.0^math.e)
# output: Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     c + (2.0^math.e)
# TypeError: unsupported operand type(s) for ^: 'float' and 'float'

c + (2^int(math.e))
17

import cmath
val = cmath.phase(c)
# output: 0.0

val = cmath.phase(4+7j)
# output: 1.0516502125483738