import numpy as np

arr = np.array([[10, 25, 30, 45],[15, 20, 35, 40],[50, 60, 55, 70],[80, 75, 90, 65]])

print(arr)   # output = [[10 25 30 45]
#                         [15 20 35 40]
#                         [50 60 55 70]
#                         [80 75 90 65]]

print(arr.ndim)    # 2

print((arr.shape))  # (4, 4)

print((arr.size))   # 16

print(arr.dtype)  # int64

print(arr[1][2])  # 35  rows * column

print(arr[0])     # [10 25 30 45]

print(arr[3])     # [80 75 90 65]

print(arr[:,0])   # [10 15 50 80]

print(arr[1:3,1:3])   # [[20 35]
                        #   [60 55}]

print(np.sum(arr))      # 765

print(np.max(arr))      # 90

print (np.min(arr))     # 10

print (np.mean(arr))    # 47.8125

print(np.sum(arr, axis=1))   # [110 110 235 310]

print(np.sum(arr, axis=0))  # [155 180 210 220]

print (np.argmax(arr))      # 14

print((np.argmin(arr)))     # 0

print(np.sort(arr, axis=1))   # [[10 25 30 45]
                                 # [15 20 35 40]
                                 # [50 55 60 70]
                                 # [65 75 80 90]]

print(np.argsort(arr, axis=1))   # [[0 1 2 3]
                                  # [0 1 2 3]
                                  # [0 2 1 3]
                                  # [3 1 0 2]]
                            
print( (np.square(arr)))          # [[ 100  625  900 2025]
                                    #  [ 225  400 1225 1600]
                                    #  [2500 3600 3025 4900]
                                    #  [6400 5625 8100 4225]]

print(np.sqrt(arr))              # [[3.16227766 5.         5.47722558 6.70820393]
                                    #  [3.87298335 4.47213595 5.91607978 6.32455532]
                                    #  [7.07106781 7.74596669 7.41619849 8.36660027]
                                    #  [8.94427191 8.66025404 9.48683298 8.06225775]]

print(arr.reshape(2, 8))         # [[10 25 30 45 15 20 35 40]
                                   #  [60 55 70 80 75 90 65]]