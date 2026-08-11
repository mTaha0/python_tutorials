import numpy as np

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]])

#- > row selection
#print(array[start:end:step]) 

# 0 dan başlayıp 2 adımda bir yazdır
print(array[0::2])

#tersten başla
print(array[::-1])

print("-"*40)
# coloumn selection
# array[row, coloumn]
# array[start:end:step ,start:end:step]


array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9],
                  [10,11,12]])

print(array[:,0])

#ikinci satırdan  ve 2. sütundan başla
print(array[2:, 2:])