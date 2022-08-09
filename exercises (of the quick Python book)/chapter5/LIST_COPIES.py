'''
Suppose that you have the following list: x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
What code could you use to get a copy y of that list in which you could change the elements without the side effect of
changing the contents of x?
'''
import copy

ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deepls = copy.deepcopy(ls)

deepls[1][2] = 'test01'
deepls[0][0] = 'test02'
print(deepls)
print(ls)