import numpy as np

# Scalar Arithmetic 


array = np.array([1.5544 ,2.9545 ,3.8455 ,4.7442])
print(array + 1)
print(array * 2)
print(array / 2)
print(array ** 1)
print(array % 3)

print("-"*40)

print(np.sqrt(array))
print(np.round(array,decimals=2))
print(np.floor(array)) # en yakın alt değer
print(np.ceil(array))  # en yakın üst değer

print("-"*40)
# EXERCISE 

print(np.pi*array**2) #pi.r^2

# ELEMENT-WISE OPERATIONS

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# COMPARISON OPERATORS

values = np.array([60, 70, 80, 100, 45])
print(values == 100)
print(values > 50)

#istenilen koşula uymuyorsa karşısındaki değere eşitle
values[values < 60] = 0
print(values)