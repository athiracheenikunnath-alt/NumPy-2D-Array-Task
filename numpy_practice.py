# numpy
# ======

import numpy as np

# array
# ======
# array_name = np.array([])

# elements = np.array([1,2,3,4])  # array contains a single row of elememnts it can be termed as 1-dimensional array
# print(elements)     # [1 2 3 4]  >>> it will give the outputs as removing the ,
# print(elements.ndim)   # 1 dimensinonal >>> here "ndim" represemts the number of dimensions in it and also it will not need () becase it is a attribute
# print(elements.shape)

# two dimensional array
# ======================

# array contains 2 row of elements like rows and columns(table like format)
# np.array([[row_1],[row_2]])


# elements_2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(elements_2)
# print(elements_2.ndim)
# print(elements_2.shape)


# three dimensionl array
# =======================

# contains multiple 2 dimensional arrays
# np.array([
#     [[row_1],[row_2]],
#     [[row_1],[row_2]]
# ])


# elements_3 = np.array([
#     [[1,2,3,4],[5,6,7,8]],
#     [[1,2,3,4],[5,6,7,8]],
#     [[1,2,3,4],[5,6,7,8]]
# ])
# print(elements_3)
# print(elements_3.ndim)


# attribites
# ===========
# print(elements_3.ndim)     # ndim represents which dimension is that  >>> out = 3

# print(elements_3.dtype)    # dtype shows the datatype that prensent in the rows and hoe much number is there  >>> out = int64

# print(elements_3.shape)    # insdie a tuple it first mention number of 2 dimentinal array,2nd it will show number 
#                            # of rows in each array, 3rd it will show number of columns  >>> out = (3, 2, 4)
                           

# =============================================================================================================================

# types of matrix
# ==================


# zero matrix
# ============

m_1 = np.zeros((3,4),dtype = int)
print(m_1)  



# ones matrix
# ============

m_2 = np.ones((3,4),dtype = int)
print(m_2)



# fill matrix
# ============
# np.full(shape,value,dtype)

m_3 = np.full((3,4),5,dtype = int)
print(m_3)



# identity matrix
# ================
# rows and columns should be equal

# np.identity
# ============
m_4 = np.identity(n = 3,dtype = int)
print(m_4)

# np.eye
# =======
m_5 = np.eye(N=4,dtype = int)
print(m_5)