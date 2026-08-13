#multidimensional arrays and indexing 

import numpy as np

print(np.__version__)

liste = [1,2,3,4]
print(liste*2) 

array = np.array([1,2,3,4])
print(array*2)
print(type(array))

array = np.array("a")
print(array.ndim)

array = np.array([[[["A"],["B"],["C"]]]])
print("+ ",array.ndim)

array = np.array([["A","B","C"], #2x3 matris
                  ["A","B","C"]])
print(array.ndim)
array = np.array([["A","B","C"], #
                  ["A","B","C"],
                  ["A","B","C"]])

print(array.shape)
print(array.ndim)

array = np.array([[["A","B","C"], #tensör
                   ["A","B","C"],
                   ["A","B","C"]]])
print(array.ndim)

array = np.array([ [["A","B","C"],["D","E","F"],   ["13","14","15"]],
                   [["1","2","3"],["7","8","9"],   ["16","17","18"]],
                   [["4","5","6"],["10","11","12"],["19","20","21"]]])

print(array[1,1,1])


array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]])

#array[start:end:step]


 
print(array[1:])
print(array[:,0])

array = np.array([[1,2,3],[2,5,6],
                  [1,2,3],[2,5,6]])
print(array.shape)
