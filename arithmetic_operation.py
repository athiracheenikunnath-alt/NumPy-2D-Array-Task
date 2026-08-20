# Arithmetic operations
# ======================

import numpy as np

# a = np.array([[3,2,4,1],[6,7,3,8]])
# b = np.array([[1,2,3,4],[5,6,7,8]])

# print(a)
# print(b)

# addition
# =========
# print(np.add(a,b))
# print(a + b)

# subrsction
# ===========
# print(np.subtract(a,b))

# multiplycation
# ===============
# print(np.multiply(a,b))

# divisition
# ===========
# print(np.divide(a,b))

# square
# =======
# print(np.sqrt(a))
# print(np.square(a))


a = np.array([[3,2,4,1],[6,4,3,1]])

print(a * 2)               # each element in array has been multiply with 2 and return result in a array
print(a ** 2)              # vector calculation
print(a / 2)


# sum
# ====
# return sum of all elements in the array

print(np.sum(a))   # 24


# axis
# =====
# sum of all elements in row wise  

print(np.sum(a,axis=1))     # [10,14]   >>> sum of all elements in row wise  

print(np.sum(a,axis=0))     # [9 6 7 2]  >>> sum of all elements in column wise


# sorting in array
# =================

# arrange the elements in ascending or descending order

print(np.sort(a))   # [[1 2 3 4]   it will give in ascending order
                        #  [1 3 4 6]]

rev = np.sort(a,axis= 1)[:,::-1]    # [[4 3 2 1]    it will give in descending order
                                    #   [6 4 3 1]]
print(rev)    # we are using slicing technique so need to give row index and column index like [0,::-1] and all

# ============================================================================================================================

arr = np.arange(1,21).reshape(5,4)
print(arr)

# output
#column index     0  1  2  3
#              [[ 1  2  3  4]  -> 0
#               [ 5  6  7  8]  -> 1
#               [ 9 10 11 12]  -> 2
#               [13 14 15 16]  ->3
#               [17 18 19 20]] -> 4   row index

# we need to select a specific column and row from the output
# slicing  syntex
# ================
# arr[row_start:row_stop:step,column_start:column_stop:step]

print(arr[1:3,1:3])     # output
                        # [[ 6  7]
                        #  [10 11]]

print(arr[2:4,1::])     # output
                        # [[10 11 12]
                        #  [14 15 16]]   

print(arr[1:4,2::])     # output
                        # [[ 7  8]
                        #  [11 12]
                        #  [15 16]]

print(arr[1:4,0:2])     # output
                        # [[ 5  6]
                        #  [ 9 10]
                        #  [13 14]]

# argsort
# ========
# it will return the index positions in the ascending order or sort order

arr_2 = np.array([4,3,5,7,2,10])
print(arr_2.argsort())             # [4 1 0 2 3 5]

# argmax
# =======
# it will return the index of largest element in the list

print(arr_2.argmax())      # 5

# argmin
# =======
# it will return the index of smallest element in the list

print(arr_2.argmin())      # 4


