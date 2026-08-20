# build a 3 / 4 order array
# ==========================
import numpy as np

arr = np.array([[3,10,11,9],[2,5,1,7],[6,14,4,8]])

print(arr.argmax())     # 9 will return here it will take the largest elements index position
                        #return the index after flatten the 2d array

print(arr.argmax(axis= 0))  # [2 2 0 0]  here it will return largest elements  index in column wise 

print(arr.argmax(axis= 1))  # [2 3 1]   here it will return largest elements  index in row wise


# where
# =====
# np.where(condition)
# used to positionong the elements which satisfy the condition

arr_2 = np.array([4,3,5,7,2,10])
print(np.where(arr_2 > 5))      # (array([3, 5]),)

# 2dimention where
# ===================

b = np.array([[3,10,11,9],[2,5,1,7],[6,14,4,8]])
print(np.where(b > 5))      
# output  
        #  row_index                      column_index
# (array([0, 0, 0, 1, 2, 2, 2]), array([1, 2, 3, 3, 0, 1, 3]))

# replace where if it accept the condition
# ==========================================
# np.where(condition,value_if_true,value_if_false)
# replace the elements from the array those satisfy condition

print(np.where( b > 5,"pass","fail"))

# output
# [['fail' 'pass' 'pass' 'pass']
#  ['fail' 'fail' 'fail' 'pass']
#  ['pass' 'pass' 'fail' 'pass']]

# sorted
# =======

c =  np.array([[3,10,11,9],[2,5,1,7],[6,14,4,8]])

