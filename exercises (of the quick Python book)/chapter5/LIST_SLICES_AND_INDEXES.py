#LIST_SLICES_AND_INDEXES
"""
Using what you know about the len()
function and list slices, how would you combine the two to get the second half of a list when you do not know what size it is?
"""
ls = [1, 2, 3, 4, 5, 6, 7]
print(ls[len(ls)//2:])
