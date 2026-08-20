# addition ,subtr
# a = np.array([1,2,3,4,5,6,7,8,9,10])
import numpy as np
a = np.array([i for i in range(1,11)])
print(a)
print(a.reshape((2,5)))


# arange
# =======

b = np.arange(1,9)
print(b)          # [1 2 3 4 5 6 7 8]

# reshape
# ========
# used to converting onedimension array into 2-d array

c = np.arange(1,9).reshape(2,4).ndim
print(c)         # 2

# flatten
# ========
# converting 2-d / 3-d array into 1-d array

b = np.array([[1,2,3,4],[5,6,7,8]])
print(b.flatten())    # [1 2 3 4 5 6 7 8]  normaly it is a 2 dimentional array it convert to one dimentional array

