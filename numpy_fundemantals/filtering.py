import numpy as np


array = np.array([[15,27,33,44,59,64,77,82,90]])

# Boolean Indexing

teenagers = array[array < 20]
print(teenagers)

adults = array[(array >= 18) & (array < 65)]
print(adults)

ages = array[(array < 34) | (array > 77)]
print(ages)


ages = np.where(array < 60, array,0)

